#!/usr/bin/env python3
"""
Research agent script for daily competitive intelligence refresh.
Calls Claude API directly to gather and synthesize research data.
"""
import sys
import json
import pathlib
from datetime import datetime
from anthropic import Anthropic

# Initialize Anthropic client
client = Anthropic()

def load_existing_json(brand: str) -> dict:
    """Load existing research JSON for a brand."""
    path = pathlib.Path(f"research/{brand}.json")
    if path.exists():
        return json.loads(path.read_text())
    return {}

def save_research_json(brand: str, data: dict) -> None:
    """Save research JSON with proper formatting."""
    path = pathlib.Path(f"research/{brand}.json")
    path.parent.mkdir(parents=True, exist_ok=True)
    # Validate JSON before saving
    json.dumps(data)  # This will raise if invalid
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False))
    print(f"✅ Saved research/{brand}.json")

def run_research_agent(brand: str) -> dict:
    """
    Run research agent for a specific brand using Claude API.
    Returns updated research JSON.
    """
    existing_data = load_existing_json(brand)

    # Determine brand-specific details
    brand_details = {
        "cardo": {
            "name": "Cardo Systems",
            "website": "https://cardosystems.com",
            "handles": {
                "instagram": "cardosystems",
                "facebook": "CardoSystems",
                "youtube": "@CardoSystemsGlobal",
                "facebook_group": "Cardo Systems Community"
            }
        },
        "sena": {
            "name": "Sena",
            "website": "https://www.sena.com",
            "handles": {
                "instagram": "senabluetooth",
                "facebook": "SenaBluetooth",
                "youtube": "@SenaBluetooth",
                "facebook_group": "Sena Bluetooth Users"
            }
        },
        "asmax": {
            "name": "ASMAX",
            "website": "https://asmaxworld.com",
            "handles": {
                "instagram": "asmaxworld_official",
                "facebook": "ASMAX",
                "youtube": "@asmaxworld",
                "facebook_group": "ASMAX Users"
            }
        },
        "reso": {
            "name": "Reso",
            "website": "https://resosport.com",
            "handles": {
                "instagram": "resoglobal",
                "facebook": "Reso",
                "youtube": "@RESOMoto",
                "facebook_group": "Reso Community"
            }
        }
    }

    details = brand_details.get(brand, {})

    prompt = f"""You are a competitive intelligence analyst researching {details.get('name', brand)}.

TASK: Update the research JSON for {brand} with the latest information gathered today.

EXISTING DATA: {json.dumps(existing_data, indent=2)}

TODAY'S DATE: {datetime.now().strftime('%Y-%m-%d')}

RESEARCH REQUIREMENTS:
1. Check {details.get('website')} for new product launches and pricing
2. Search for recent press coverage (motorcycle magazines: MCN, webBikeWorld, RevZilla, FortNine, Bennetts, RideApart)
3. Look for firmware/app updates via release notes and app stores
4. Check social media: Instagram @{details.get('handles', {}).get('instagram')}, YouTube, Reddit r/motorcyclegear
5. Verify real customer feedback (no fabrication)

OUTPUT REQUIREMENTS:
- Return ONLY valid JSON (no markdown, no explanation)
- Preserve existing schema - only update values, never rename/remove keys
- All dates in YYYY-MM-DD format
- All URLs must be real and working
- No smart quotes - use straight ASCII only
- Never fabricate data - if unsure, use null or skip
- New products must include full 16-dimension capability matrix in dimensions object
- Firmware updates must have real version numbers and URLs

CRITICAL RULES:
- Do NOT invent products, prices, or customer feedback
- Do NOT create fake URLs - verify everything is real
- Use null for unknown values rather than guessing
- Keep all existing keys, only update values

Return the complete updated JSON for {brand}."""

    print(f"🔄 Calling Claude API for {brand.upper()} research...")

    # Use streaming for longer outputs
    full_response = ""
    with client.messages.stream(
        model="claude-opus-4-8",
        max_tokens=32000,
        messages=[{"role": "user", "content": prompt}]
    ) as stream:
        for text in stream.text_stream:
            full_response += text
            # Print progress dots
            if len(full_response) % 500 == 0:
                print(".", end="", flush=True)
        stop_reason = stream.get_final_message().stop_reason

    print()  # Newline after dots

    if stop_reason == "max_tokens":
        print(f"⚠️ Response for {brand} was cut off at max_tokens ({len(full_response)} chars received)")

    # Parse the JSON response
    try:
        # Find JSON in the response (Claude might include explanation)
        json_start = full_response.find('{')
        json_end = full_response.rfind('}') + 1
        if json_start >= 0 and json_end > json_start:
            json_str = full_response[json_start:json_end]
            updated_data = json.loads(json_str)
            print(f"✅ Parsed {brand} research data from Claude")
            return updated_data
        else:
            print(f"⚠️ No JSON found in Claude response for {brand}, keeping existing data")
            return existing_data
    except json.JSONDecodeError as e:
        print(f"⚠️ Failed to parse JSON response for {brand}: {e}")
        print(f"   Keeping existing data")
        return existing_data

def validate_research_data(brand: str, data: dict) -> bool:
    """Validate research JSON structure."""
    required_keys = ["competitor", "website", "company", "products", "strengths",
                     "weaknesses", "recent_news", "social_media", "press_coverage"]

    missing = [k for k in required_keys if k not in data]
    if missing:
        print(f"⚠️ Warning: {brand} JSON missing keys: {missing}")
        return False

    if not isinstance(data.get("products"), list):
        print(f"⚠️ Warning: {brand} products is not a list")
        return False

    # Validate that JSON is serializable
    try:
        json.dumps(data, ensure_ascii=False)
        return True
    except Exception as e:
        print(f"⚠️ Warning: {brand} JSON is not serializable: {e}")
        return False

def main():
    if len(sys.argv) < 2:
        print("Usage: python research_agent.py <brand> (cardo|sena|asmax|reso)")
        sys.exit(1)

    brand = sys.argv[1].lower()
    if brand not in ["cardo", "sena", "asmax", "reso"]:
        print(f"Invalid brand: {brand}")
        sys.exit(1)

    print(f"\n{'='*60}")
    print(f"Research Agent: {brand.upper()}")
    print(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}")
    print(f"{'='*60}\n")

    try:
        # Run research
        updated_data = run_research_agent(brand)

        # Validate
        if validate_research_data(brand, updated_data):
            # Save
            save_research_json(brand, updated_data)
            print(f"\n✅ {brand.upper()} research agent completed successfully")
        else:
            print(f"\n⚠️ {brand.upper()} research has validation issues but was saved")
            save_research_json(brand, updated_data)

    except Exception as e:
        print(f"\n❌ Error in {brand.upper()} research agent: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
