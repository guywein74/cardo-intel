# ASMAX — Competitive Intelligence Notes (for Cardo Systems)

Research date: 2026-07-02. Companion data file: `/Users/guyw/Desktop/Claude/Cardo/research/asmax.json`

## 1. Who they are

- **Legal entity / HQ:** Shenzhen Asmax Infinite Technology Co., Ltd., Room 803, Building B4, Keyling Science Park, Shenzhen, China. Corporate contact email uses the domain `max-limits.com`, suggesting a parent/affiliate named Max-Limits.
- **Founding:** Brand officially launched in China in **2023**; company claims "20+ years of mobile R&D / IoT expertise" (asmaxworld.com marketing also says "founded in 2004" — likely referring to the ODM/parent's history, not the brand). Treat the 2004 date as marketing.
- **Funding:** No funding rounds, investors, or parent-company financials disclosed anywhere. Appears self-funded / ODM-backed.
- **Scale claims (self-reported):** "Fastest growing smart-helmet Bluetooth headset brand in China," 30+ countries, 2,000+ partner stores, 100,000+ connected riders.
- **Important correction to the brief:** ASMAX does **not** sell a smart helmet, and there is no "ASMAX X1 smart helmet." (The X1 smart helmet found in searches is CrossHelmet, an unrelated Japanese company.) ASMAX sells clamp-on/magnet-mount **helmet intercoms**, smart **air pumps**, and audio-kit accessories, marketed together as a "Smart Riding IoT Ecosystem" with helmets and cameras named as future ecosystem targets. Their site mentions Insta360 wireless audio integration.

## 2. Web presence (fragmented — three sites)

| Site | Role |
|---|---|
| asmaxworld.com | US/DTC Shopify store — currently sells only F1s, S1 (+ Z1 previously, now 404), pumps, kits |
| asmaxconnect.com | Newer global brand site — full 2025-26 lineup incl. F1 Pro Max, Future 1 (EVA R), S2, "X Pro", MAXRUNON sub-brand |
| asmaxmoto.com | Corporate/brand site (history, technology, EICMA PR contact) |

Retail: Amazon US, Amazon JP, AliExpress/Alibaba, SE Asia dealer networks (Malaysia — Takong Racing, Bikers Stop Rawang, Kawasaki Setapak; Philippines; Singapore — Regina Specialties), EU e-tail (Chromeburner).

## 3. Product line detail (gaps noted)

### US-market (asmaxworld.com, launched 2024)
- **F1s** — list $226.99 / street **$139.99**. Mesh + BT5.3 dual chip, 10 riders, "5-mile" claim, IP67, 1,250 mAh, 10 min charge = 3 h intercom, 50 min full charge, 50 g, offline "Hi Max" AI voice (EN/ES/JA), CloudTalk cross-brand/cloud mode, Insta360 audio, Aura LED, FOTA, 2-yr warranty. Exact talk-time hours not published on the US page (F1-family listings elsewhere cite ~14 h intercom / ~21 h music).
- **S1** — list $121.99 / street **$89.99–92.88**. Mesh + BT5.4, 8 riders (up to 50 in ASMAX/CloudTalk cloud modes), IPX7, 980 mAh, **13 h intercom / 16 h music / 96 h standby**, FM radio, 41 g, offline AI voice, 2-yr warranty.
- **Z1 / Z1 Plus** — ~$89.99 US / RM699 MY. BT5.3, 10 riders, 40 mm HiFi speakers, 1,050 mAh, IP67, claimed "15 km/9 mi" (chained mesh marketing). Z1 page now 404 on the US store — possibly discontinued/superseded by S2.
- The original **F1** (2024, from $119.99) has been replaced by the F1s.

### 2025–26 global lineup (EICMA 2025; not yet on US store as of Jul 2026)
- **F1 Pro** — RM899 (~$190) / SGD279 (~$205, list SGD379). BT5.3 dual-chip octa-core, 10 riders, 3 km claim, **14 h intercom / 21 h music**, IPX7, Bongiovi "Grammy-level" tuning, voice + Siri/Google.
- **F1 Pro Max** — top model: **45 mm** rear-sound-cavity speakers, 1,350 mAh, BT5.3, 10-rider mesh, AI voice. **No confirmed USD price found** (AliExpress listing exists; page blocked).
- **Future 1** — RM699 (~$150–160). BT5.4 dual-chip octa-core, 10 riders, "within 3 km," 40 mm speaker, 1,350 mAh, ~3 h talk per full charge per one dealer spec sheet vs "~14 h continuous talk" on Amazon JP — dealer sheet likely conflated fast-charge figures; JP figure (14 h) is more consistent with the platform. IPX7, neural-net ENC clear to 160–180 km/h, 50 g.
- **Future 1 EVA R** — official **Evangelion Racing** collaboration (Evangelion 30th anniversary), launched **Nov 1, 2025** in Japan through an exclusive distributor; four colorways (Unit-01/Unit-02 motifs); same Future 1 platform (BT5.4, 10 riders, ~14 h talk). Sold on Amazon.co.jp; JPY price not captured.
- **S2** — entry mesh: BT5.4 dual chip, 8 riders team mode / **50 riders network (cloud) mode**, 3 km, 40 mm "MAX TUNING" speaker, 980 mAh, 16–18 h music / 10–12 h music+intercom / 4–5 day standby, IPX7, FM, auto-volume, 41 g. On Amazon US and Chromeburner (EU); price not captured.
- **X Pro** — listed on asmaxconnect.com nav as a helmet-intercom model; no specs/price found anywhere. Watch item.
- **MAXRUNON 2X / D10** — outdoor-sports intercom sub-brand with separate MAXRUNOS app.
- **Pumps:** T10 inflator $58.99, T20 jump-starter+inflator $84.99, T30 mini $52.99 (all heavily "discounted" from ~$110–130 list).

Pricing pattern: permanent deep "sales" off inflated list prices — anchor pricing typical of Amazon-native Chinese brands.

## 4. Technology & AI vs. Cardo/Sena (conceptual)

- **"Hi Max" offline AI voice assistant:** on-device, no phone/internet needed, EN/ES/JA. Functionally similar in concept to Cardo Natural Voice, but ASMAX leans harder on voice as the *primary* UI (creating/joining groups, EQ, LED, music by voice) because its hardware has fewer buttons and no roller wheel. Reviewers (PHToll S1 review) confirm commands register reliably at highway speed with gloves — this is their most credible differentiator at the price.
- **CloudTalk / "MESH + 5G" SMC:** patented ("global exclusive invention patent") intelligent seamless switching between local mesh and cellular cloud intercom via the ASMAX World app — up to **50 riders**, effectively unlimited range where there is coverage. Conceptually equivalent to app-based bridges (Sena Meshport-style / phone-app intercoms) but integrated natively. Weakness: dead without cellular coverage; adds phone/data dependency.
- **Smart Mesh Control (SMC) next-gen:** previewed at AIMExpo 2026 — dynamic real-time group management as riders join/drop/reorder; **full launch expected later in 2026**. This is the roadmap item to monitor most closely; it targets Cardo DMC's core strength (self-healing mesh).
- **Audio:** Bongiovi Acoustic Labs ("Grammy-level") tuning on 2025 models — their answer to Cardo's JBL and Sena's Harman Kardon partnerships. Depth of the partnership unverified.
- **Ecosystem play:** one app controlling intercoms, cameras (Insta360 audio today), pumps; FOTA across all devices. Positions ASMAX as an "IoT platform" rather than a headset maker.

## 5. Review sentiment (YouTube / forums / regional reviewers)

**Positive:** sound quality per dollar ("deep bass, zero distortion" claims largely echoed by users), offline voice control genuinely works, easy install, battery life, packaging quality, responsive customer service on warranty issues. Framed repeatedly as a "**budget Cardo**" (YouTube: "ASMAX F1 & S1 review: Better than Sena & Cardo?", Jul 2025; multiple TikTok loudness-test comparisons vs Cardo).

**Negative:**
- **Range reality gap:** advertised 5 mi / 8–15 km; measured ~0.7–1.2 km between closest riders with terrain/traffic (PHToll, Go Motorbikes).
- Mesh is ASMAX-only; mixing with Cardo/Sena requires the (single-channel) Bluetooth bridge or CloudTalk-over-cellular.
- Budget mic quality for rider-passenger; voice assistant can struggle with heavy noise/accents.
- Limited physical controls vs Cardo wheel; some complex tasks need the app.
- Scattered hardware QC complaints: magnet mount failures, base-plate adhesion, voice-activation glitches.
- Essentially zero coverage from established Western outlets (webBikeWorld, ADVrider) — low trust base among core enthusiasts; review presence is TikTok/YouTube/SE-Asia dealer blogs.

## 6. Recent news timeline

- **Jan 2026** — AIMExpo 2026, Anaheim (Booth 785): first big US trade-show push; showed F1 Pro, F1 Pro Max, Future 1, Future 1 EVA R, S2; previewed SMC (full launch "later in 2026"). PR distributed via AI Journal/newswires.
- **Nov 4–9, 2025** — EICMA 2025, Milan (Booth O84, Hall 9): unveiled the five-model 2025-26 lineup; announced Bongiovi audio tuning and MESH+5G SMC (PRNewswire).
- **Nov 1, 2025** — Future 1 EVA R Evangelion Racing collab launched in Japan (exclusive distributor; Amazon JP).
- **2025** — SE Asia dealer expansion (Malaysia/Philippines/Singapore) drove most retail visibility; Western YouTube "better than Cardo/Sena?" reviews began appearing.
- **2024** — US entry via Amazon + Shopify DTC with F1/F1s, S1, Z1 at $90–140.
- **No funding, acquisition, or OEM-partnership news found for 2025–2026.**

## 7. Implications for Cardo (analyst view)

1. **Price flank:** ASMAX undercuts Packtalk Edge-class product by ~60% while matching the spec sheet (mesh, 10+ riders, voice, IPX7, big speakers, FOTA, 2-yr warranty). Main defense today is Cardo's real-world range, DMC reliability, dealer/service network, and brand trust.
2. **Cloud intercom is the asymmetric threat:** CloudTalk's 50-rider unlimited-range cellular mode is a feature-story Cardo can't match natively; expect them to market SMC hard in 2026 US push.
3. **US push is early-stage:** flagship 2025 models still absent from the US store eight months after EICMA — execution/distribution is their current bottleneck. Window exists before F1 Pro Max/Future 1 land at US retail.
4. **Watch items:** US pricing/availability of F1 Pro Max & Future 1, SMC full launch (H2 2026), the unspecified "X Pro" model, any move into actual smart helmets/cameras, and whether they land a Western review (webBikeWorld/FortNine) that legitimizes the brand.

## 8. Data gaps (could not verify — marked null in JSON)

- Any funding/revenue figures; headcount.
- USD MSRP for F1 Pro Max, Future 1 (EVA R), S2, Z1 list price, X Pro (everything).
- F1s exact talk-time hours; F1 Pro Max waterproof rating and talk time.
- Amazon US star ratings/review counts (pages blocked to fetcher).
- Depth/exclusivity of Bongiovi and Insta360 relationships.

## Social Media

Researched 2026-07-02. Owned presence is small and fragmented (two parallel account sets mirroring the asmaxworld/asmaxconnect site split); earned dealer/creator content is where the traction is.

### Owned accounts
| Platform | Handle | Followers (Jul 2026) | Notes |
|---|---|---|---|
| Instagram | @asmaxworld_official | ~16K (356 posts) | Main account; product reels, firmware-update posts, heavy Spanish-language content for LATAM |
| Instagram | @asmaxofficial | unknown | Second account linked from asmaxconnect.com |
| Facebook | facebook.com/ASMAXWorld | ~448 likes, 14 talking about | Negligible owned FB presence; ASMAXOfficial page also exists |
| YouTube | @ASMAXWorld (+ @ASMAX.Connect) | unknown | Product/how-to content; subscriber count not retrievable |
| TikTok | none found | n/a | No official account linked from any ASMAX site |
| LinkedIn | linkedin.com/company/asmax-world | unknown | Corporate page |

### Reddit
- Essentially **invisible on Reddit** as of Jul 2026: site-restricted searches return no dedicated ASMAX threads in r/motorcycles or intercom-related subreddits; only passing mentions in budget-intercom discussions. This is the clearest evidence they haven't penetrated the Western enthusiast community where Cardo/Sena debates happen.
- Community sentiment (drawn from Amazon reviews, Facebook, YouTube comments in lieu of Reddit): praise for sound-per-dollar, working offline voice control, easy install, fast charging, responsive support; complaints about range vs claims, ASMAX-only mesh, magnet-mount/adhesion failures, weak passenger mic, limited buttons.

### Facebook ecosystem
Dealer/creator-driven rather than brand-driven: SEC Motosupply, Takong Racing KL, Moto Automain, MotorniJuan (PH) push Future 1 / EVA R / S2 launch and promo content; rider groups like Foreign Riders Thailand surface ASMAX in "which intercom" threads; small reviewers (mr19works) post quick "worth it?" reviews. Sentiment in these markets is enthusiastic and value-driven.

### YouTube reviewer coverage
- "ASMAX F1 & S1 review: Better than Sena & Cardo?" (Jul 2025) — the framing ASMAX wants
- "ASMAX F1 Motorcycle Coms System Full Review And Testing"
- "ASMAX Z1 PLUS INTERCOM — Best price-quality ratio"
- "ASMAX S1 Intercom Test 2026 — Is it really worth it"
- "Asmax Future 1 — Hi-Tech Intercom with the BEST VALUE for Money" (PH)
Common verdict: excellent value / "budget Cardo," good audio and voice control, range claims overstated. No FortNine, RevZilla, or other major-channel coverage found.

### TikTok
Likely their strongest awareness channel despite no official account: dozens of discover/hashtag pages (intercom-asmax, asmax-f1-intercom-review, **asmax-vs-cardo**, how-to-connect-cardo-intercom-to-asmax-f1), viral Cardo-vs-ASMAX loudness tests (e.g., @namesayenas), install/pairing tutorials. Heavy in Spanish-language (LATAM) and SE Asian content — a grassroots price-comparison narrative aimed directly at Cardo.

**Takeaway for Cardo:** ASMAX is winning bottom-of-funnel social search ("asmax vs cardo" TikTok pages) in emerging markets while remaining absent from Reddit and Western enthusiast spaces. Monitor for the moment a large Western creator (FortNine-class) picks them up.

## Press Coverage

### Editorial reviews found (2024-2026)
| Outlet | Date | Product | Verdict |
|---|---|---|---|
| MotoUK (via GenXrider) | n/d | F1-family intercom | Positive: 10-min install, clear to ~70 mph, ~10 h mixed battery, strong value |
| PHToll (Philippines) | 2025 | S1 | Recommended for first-time mesh buyers; great speakers, working voice control; budget mic, ~1.2 km real range vs 5-mile claim |
| Go Motorbikes | 2025 | S1 2-pack | Positive budget pick; flags real-world range 700-1,100 m |
| Bikers Stop Rawang (MY dealer) | 2025 | S2/Z1+/F1 Pro/Future 1 | Lineup buying guide; F1 Pro best runtime (21 h music / 14 h intercom) |
| MotoMelody | 2025 | F1 (mention) | Good for simplicity/voice, "may lack advanced control options" vs Cardo wheel |

### PR / news coverage
- EICMA 2025 press release (2025-11-07, PRNewswire) syndicated widely: Morningstar, Manila Times, WBTW, AI Journal, ittech-pulse — company-authored, no independent assessment.
- AIMExpo 2026 showcase (2026-01-09, AI Journal) — press-release pickup, previews SMC full launch later in 2026.

### What's missing
- **Zero coverage found in tier-1 motorcycle media:** no MCN, Cycle World, RideApart, webBikeWorld, Bennetts BikeSocial, RevZilla Common Tread, or Motorcyclist reviews or news items for 2024-2026.
- **No awards found** (no Red Dot, no EICMA innovation award, no "best intercom" list placements at major outlets).

### Overall tone
Where independent testing exists (small regional/hobbyist outlets), tone is consistently positive-for-the-price with the same caveats (range, lock-in, mic). Everything else is self-generated PR. For Cardo this means ASMAX currently has a credibility ceiling in Western markets — but their AIMExpo 2026 presence and newswire spending signal an active push to close that gap; the first major-outlet review would be the inflection point to watch.

## Dimensions data

Added 2026-07-02 per Cardo competitive-landscape format ("dimensions" key per product in asmax.json). Notes on ambiguous/derived fields:

- **Physical dimensions (mm):** not published anywhere for any model (product pages, manuals.plus manuals, retailer listings) — null across the board. Weights confirmed: F1s 50 g, S1 41 g, Future 1 50 g, S2 41 g; Z1, F1 Pro, F1 Pro Max unknown.
- **Controls:** no ASMAX model has a jog wheel/dial — all are button-operated (F1 manual documents an intercom button + volume +/- combos) with "Hi Max" voice as the intended primary interface. This is a real UX gap vs Cardo's glove-friendly roller wheel and is flagged in MotoMelody's controls guide.
- **Mounts vary by model — a differentiation nuance:** Z1 and F1 Pro / Future 1 use **magnetic** bases; the F1s is explicitly marketed as **"No-Magnet" snap-in** (likely a response to magnet-mount failure complaints on earlier units); S1 base type unspecified (adhesive/clip); F1 Pro Max and S2 mounts unconfirmed.
- **Auto-reconnect:** set to true for all mesh models based on ASMAX marketing ("Auto-reconnects, self-healing connection... kicks in instantly when back in range" on F1s/F1 pages). Independent verification exists only anecdotally (owner reviews reporting stable reconnection).
- **Wideband/HD audio:** no ASMAX model claims HD Voice/wideband intercom audio anywhere — null everywhere. Cardo's HD-quality intercom audio claim remains a differentiator on paper.
- **Speaker sizes:** 40 mm confirmed for S1, Z1, F1 Pro, Future 1 (and EVA R), S2; 45 mm for F1 Pro Max; F1s speaker size never published (likely 40 mm, left null).
- **Speaker brand:** all in-house ("ASMAX Acoustic Lab"); 2025 generation adds "Grammy-level Bongiovi Acoustic Labs" tuning claims — no branded co-engineered hardware like Cardo/JBL or Sena/Harman Kardon.
- **Warranty:** 2 years is a site-wide banner claim; explicitly confirmed on F1s, S1, Z1, S2 pages. Applied to F1 Pro / Pro Max / Future 1 / EVA R as brand policy (not individually verified).
- **Range_km values:** claimed figures (8 km US models per "5-mile" listings, 3 km for the 2025 EU/Asia models per EICMA PR — note the *newer* models claim *less*, suggesting more honest spec sheets post-EICMA). Real-world tests: 0.7-1.2 km.
- **Prices:** F1 Pro street ($205) converted from SGD 279; Future 1 ($155) from RM 699. F1 Pro Max, EVA R, S2 prices genuinely unavailable in USD — null.
- **Misc discovery:** a further model, **ASMAX VITUS** (mesh intercom), appears in a manuals.plus user manual but on no ASMAX site or retailer found — possibly OEM/regional or upcoming; worth monitoring. Also, the F1 manual notes Group (mesh) mode "supports up to 4 people" in one configuration vs the marketed 10 — mode-dependent rider caps may be smaller than headline claims.

## Sources

- https://www.asmaxworld.com/ (+ /products/f1s, /products/s1, /collections/headsets)
- https://asmaxmoto.com/ and https://asmaxmoto.com/Brand
- https://www.asmaxconnect.com/
- PRNewswire, "ASMAX Showcases Next-Gen Smart Riding IoT Ecosystem at EICMA 2025" — https://www.prnewswire.com/news-releases/asmax-showcases-next-gen-smart-riding-iot-ecosystem-at-eicma-2025-302608451.html
- AI Journal, "ASMAX Brings Rider-Centric Smart Connectivity to AIMExpo 2026" — https://aijourn.com/asmax-brings-rider-centric-smart-connectivity-to-aimexpo-2026/
- Takong Racing (MY): Future 1 (RM699), Z1 Plus (RM699), F1 Pro (RM899) product pages — mytakongracing.com
- Regina Specialties (SG): F1 Pro SGD279/379 — reginaspecialties.com
- Chromeburner (EU): S2 specs — chromeburner.com
- PHToll ASMAX S1 review — https://phtoll.com/reviews/asmax-s1-review/
- Go Motorbikes S1 review — https://gomotorbikes.com/blog/reviews/asmax-s1-intercom-review/
- Amazon US listings (F1s B0D1R1GDYP, S1 B0D7P5MF7C, Z1 B0D1RJ1JZH, S2 B0DQW9GHWQ); Amazon JP EVA R listings (B0FY69Z3MV et al.)
- Bikers Stop Rawang comparison blog (S2 vs Z1 Plus vs F1 Pro vs Future 1)
- YouTube: "ASMAX F1 & S1 review: Better than Sena & Cardo?" (B7Xp04mDVFY); "ASMAX F1 Full Review" (aCMzg9xCNvE); "ASMAX Z1 PLUS" (vfacZRjQ-x0)
- Social: instagram.com/asmaxworld_official (~16K, Jul 2026); facebook.com/ASMAXWorld (~448 likes); youtube.com/@ASMAXWorld; TikTok discover pages (tiktok.com/discover/asmax-vs-cardo et al.)
- Press: GenXrider/MotoUK review — genxrider.com; MotoMelody controls guide — motomelody.com; EICMA PR syndication — Morningstar, Manila Times, WBTW, AI Journal
