#!/usr/bin/env python3
"""
Keepa scanner — pulls full Amazon product + offers data for competitor ASINs
and writes a clean summary to research/keepa_pricing.json for the dashboard.

The Keepa Pro API key is read ONLY from the environment (KEEPA_API_KEY) or a
git-ignored .env.keepa / .env file — never hardcoded here. Claude does not read
the value.

Usage:
    python scripts/keepa_scan.py                       # all brands in the config
    python scripts/keepa_scan.py --brands cardo,sena   # subset
    python scripts/keepa_scan.py --asins B0ABC123,B0XYZ789
    python scripts/keepa_scan.py --offers 20 --stats 90

Config: research/keepa_asins.json maps each brand to a list of ASINs to track.
Docs: https://keepa.com/#!discuss/t/product-object/116
"""
from __future__ import annotations
import argparse
import json
import os
import pathlib
import sys
from datetime import datetime, timezone

ROOT = pathlib.Path(__file__).resolve().parent.parent
RESEARCH = ROOT / "research"
CONFIG_PATH = RESEARCH / "keepa_asins.json"
OUT_PATH = RESEARCH / "keepa_pricing.json"

# Keepa CSV / stats array indices (subset we care about). Prices are in cents;
# -1 means "no data". RATING is stored as stars*10 (45 -> 4.5).
IDX = {
    "amazon": 0,       # Amazon-sold price
    "new": 1,          # marketplace New (3rd-party) price
    "used": 2,
    "sales_rank": 3,   # BSR (raw rank, not a price)
    "list_price": 4,
    "rating": 16,      # stars * 10
    "review_count": 17,
    "buybox": 18,      # Buy Box price (incl. shipping)
}


# ─────────────────────────── env / key loading ───────────────────────────
def _load_env_files() -> None:
    """Load KEEPA_API_KEY from .env.keepa / .env into os.environ if not already
    set. Minimal parser (no dependency); values are never printed."""
    for name in (".env.keepa", ".env"):
        p = ROOT / name
        if not p.exists():
            continue
        for line in p.read_text().splitlines():
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            k, _, v = line.partition("=")
            k, v = k.strip(), v.strip().strip('"').strip("'")
            os.environ.setdefault(k, v)


def get_api_key_or_none() -> str | None:
    """Non-fatal key lookup for library use (e.g. from research_agent.py) —
    callers decide how to handle a missing key instead of the process exiting."""
    _load_env_files()
    return os.environ.get("KEEPA_API_KEY") or os.environ.get("KEEPA_KEY")


def get_api_key() -> str:
    """CLI entry point: exits with a helpful message if the key is missing."""
    key = get_api_key_or_none()
    if not key:
        sys.exit(
            "KEEPA_API_KEY not set.\n"
            "  Put it in a git-ignored file:  echo 'KEEPA_API_KEY=your_pro_key' > .env.keepa\n"
            "  or export it:                  export KEEPA_API_KEY=your_pro_key"
        )
    return key


def fetch_brand_pricing(brand: str, offers: int = 0, stats: int = 90, domain: str = "US") -> dict | None:
    """Library entry point for other agents (e.g. research_agent.py): fetch this
    brand's current Amazon pricing/BSR/rating snapshot via Keepa.

    Never raises — returns None (with a printed warning) if the API key isn't
    configured, the brand has no ASINs, or the Keepa request fails, so a
    calling agent's run is never blocked by Keepa being unavailable.

    offers=0 (default) skips offer-listing data to keep token cost minimal for
    routine automated runs; pass offers=20-100 for full buy-box/offer detail.
    """
    api_key = get_api_key_or_none()
    if not api_key:
        print(f"  [keepa] KEEPA_API_KEY not set — skipping Amazon pricing for {brand}")
        return None

    try:
        cfg = load_config()
    except SystemExit as e:
        print(f"  [keepa] {e} — skipping Amazon pricing for {brand}")
        return None

    asins = cfg.get(brand, [])
    if not asins:
        print(f"  [keepa] No ASINs configured for {brand} in {CONFIG_PATH.name} — skipping")
        return None

    offers_param = None if offers == 0 else offers
    try:
        import keepa
        api = keepa.Keepa(api_key)
        products = api.query(asins, domain=domain, offers=offers_param, stats=stats, rating=True, history=False)
    except Exception as e:  # network error, rate limit, invalid ASIN batch, etc.
        print(f"  [keepa] Fetch failed for {brand}: {e} — skipping Amazon pricing")
        return None

    by_asin = {p.get("asin"): p for p in products}
    items = [summarize(by_asin[a], offers or 0) for a in asins if a in by_asin]
    missing = [a for a in asins if a not in by_asin]
    if missing:
        print(f"  [keepa] {brand}: no data for {missing}")

    print(f"  [keepa] {brand}: fetched {len(items)}/{len(asins)} ASIN(s), tokens left: {getattr(api, 'tokens_left', '?')}")
    return {
        "fetched_at": datetime.now(timezone.utc).isoformat(),
        "domain": domain,
        "products": items,
    }


# ─────────────────────────── value helpers ───────────────────────────
def cents(v) -> float | None:
    """Keepa price (cents, -1 = none) -> dollars, or None."""
    if v is None or v == -1:
        return None
    try:
        return round(float(v) / 100.0, 2)
    except (TypeError, ValueError):
        return None


def stat(stats: dict, bucket: str, idx: int):
    """Pull stats['current'|'avg'|'min'|'max'][idx] safely."""
    arr = (stats or {}).get(bucket)
    if not isinstance(arr, (list, tuple)) or idx >= len(arr):
        return None
    val = arr[idx]
    # min/max entries can be [timestamp, value] pairs in some responses
    if isinstance(val, (list, tuple)):
        val = val[-1] if val else None
    return val


def summarize_offers(product: dict, limit: int) -> list[dict]:
    out = []
    for o in (product.get("offers") or [])[:limit]:
        csv = o.get("offerCSV") or []
        price = None
        if len(csv) >= 2:
            # offerCSV = [time, price, (shipping), ...]; take the latest price
            price = cents(csv[-2] if len(csv) % 3 == 0 else csv[-1])
        out.append({
            "sellerId": o.get("sellerId"),
            "price": price,
            "condition": o.get("condition"),
            "isFBA": o.get("isFBA"),
            "isPrime": o.get("isPrime"),
            "isBuyBoxWinner": o.get("isBuyBoxWinner"),
        })
    return out


def summarize(product: dict, offers_limit: int) -> dict:
    stats = product.get("stats") or {}
    rating_raw = stat(stats, "current", IDX["rating"])
    return {
        "asin": product.get("asin"),
        "title": product.get("title"),
        "brand": product.get("brand"),
        "manufacturer": product.get("manufacturer"),
        "current": {
            "amazon": cents(stat(stats, "current", IDX["amazon"])),
            "new": cents(stat(stats, "current", IDX["new"])),
            "buybox": cents(stat(stats, "current", IDX["buybox"])),
            "buybox_seller": product.get("buyBoxSellerId"),
            "list_price": cents(stat(stats, "current", IDX["list_price"])),
            "sales_rank": stat(stats, "current", IDX["sales_rank"]),
            "rating": round(rating_raw / 10, 1) if isinstance(rating_raw, (int, float)) and rating_raw > 0 else None,
            "review_count": stat(stats, "current", IDX["review_count"]),
            "offer_count": product.get("offerCount") or len(product.get("offers") or []),
        },
        "range_new": {
            "min": cents(stat(stats, "min", IDX["new"])),
            "max": cents(stat(stats, "max", IDX["new"])),
            "avg": cents(stat(stats, "avg", IDX["new"])),
        },
        "range_buybox": {
            "min": cents(stat(stats, "min", IDX["buybox"])),
            "max": cents(stat(stats, "max", IDX["buybox"])),
            "avg": cents(stat(stats, "avg", IDX["buybox"])),
        },
        "sales_rank_avg": stat(stats, "avg", IDX["sales_rank"]),
        "category": product.get("categoryTree", [{}])[-1].get("name") if product.get("categoryTree") else None,
        "offers": summarize_offers(product, offers_limit),
        "keepa_url": f"https://keepa.com/#!product/1-{product.get('asin')}",
    }


# ─────────────────────────── main ───────────────────────────
def load_config() -> dict:
    if not CONFIG_PATH.exists():
        sys.exit(f"Missing {CONFIG_PATH}. Add ASINs per brand there first.")
    cfg = json.loads(CONFIG_PATH.read_text())
    return {k: v for k, v in cfg.items() if not k.startswith("_")}


def main() -> None:
    ap = argparse.ArgumentParser(description="Fetch Amazon product+offers via Keepa.")
    ap.add_argument("--brands", help="comma-separated subset of brands from the config")
    ap.add_argument("--asins", help="comma-separated ASINs (bypasses the config)")
    ap.add_argument("--offers", type=int, default=20,
                     help="offers to request per ASIN, 20-100 (more = more tokens). "
                          "Use 0 to skip offer data entirely (cheapest — product+stats only).")
    ap.add_argument("--stats", type=int, default=90, help="stats window in days")
    ap.add_argument("--domain", default="US", help="Amazon domain (US, CO.UK, DE, ...)")
    args = ap.parse_args()

    # Keepa's API only accepts offers=None (skip) or an int in [20, 100].
    offers_param: int | None
    if args.offers == 0:
        offers_param = None
    elif 20 <= args.offers <= 100:
        offers_param = args.offers
    else:
        sys.exit("--offers must be 0 (skip offer data) or between 20 and 100.")

    import keepa  # imported here so --help works without the dep

    api = keepa.Keepa(get_api_key())

    # Build brand -> [asins]
    if args.asins:
        brand_asins = {"adhoc": [a.strip() for a in args.asins.split(",") if a.strip()]}
    else:
        cfg = load_config()
        wanted = [b.strip() for b in args.brands.split(",")] if args.brands else list(cfg)
        brand_asins = {b: cfg.get(b, []) for b in wanted}

    all_asins = sorted({a for lst in brand_asins.values() for a in lst})
    if not all_asins:
        sys.exit("No ASINs to fetch. Add them to research/keepa_asins.json (or pass --asins).")

    print(f"Keepa: fetching {len(all_asins)} ASIN(s), offers={offers_param}, stats={args.stats}d, domain={args.domain}")
    products = api.query(
        all_asins, domain=args.domain, offers=offers_param,
        stats=args.stats, rating=True, history=False,
    )
    by_asin = {p.get("asin"): p for p in products}

    result = {
        "fetched_at": datetime.now(timezone.utc).isoformat(),
        "domain": args.domain,
        "tokens_left": getattr(api, "tokens_left", None),
        "brands": {},
    }
    for brand, asins in brand_asins.items():
        result["brands"][brand] = [
            summarize(by_asin[a], offers_param or 0) for a in asins if a in by_asin
        ]
        missing = [a for a in asins if a not in by_asin]
        if missing:
            print(f"  ! {brand}: no data for {missing}")

    OUT_PATH.write_text(json.dumps(result, indent=2, ensure_ascii=False))
    n = sum(len(v) for v in result["brands"].values())
    print(f"Wrote {n} product(s) -> {OUT_PATH.relative_to(ROOT)}  (tokens left: {result['tokens_left']})")


if __name__ == "__main__":
    main()
