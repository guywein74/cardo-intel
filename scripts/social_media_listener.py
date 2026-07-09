#!/usr/bin/env python3
"""
Social Media Listener agent - collects real customer feedback from forums.
Runs as part of daily refresh to append new customer_feedback to brand JSONs.
"""
import sys
import json
import pathlib
from datetime import datetime
from anthropic import Anthropic

client = Anthropic()

def load_brand_json(brand: str) -> dict:
    """Load existing brand research JSON."""
    path = pathlib.Path(f"research/{brand}.json")
    if path.exists():
        return json.loads(path.read_text())
    return {}

def save_brand_json(brand: str, data: dict) -> None:
    """Save brand research JSON."""
    path = pathlib.Path(f"research/{brand}.json")
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False))

def run_social_media_listener() -> dict:
    """
    Run Social Media Listener agent - gathers customer feedback across all brands.
    Returns dict with feedback arrays to append to each brand JSON.
    """

    prompt = """You are a Social Media Listener agent gathering real customer feedback across motorcycle intercom brands.

TODAY'S DATE: """ + datetime.now().strftime('%Y-%m-%d') + """

TASK: Search for and collect NEW customer feedback from Reddit r/motorcyclegear (public, searchable).

Facebook Group and Instagram feedback is handled separately by scripts/apify_social_listener.py,
which uses real Apify scraper actors rather than this model's own recall - do not attempt to
generate Facebook content here, it has no way to verify real posts exist.

SEARCH TERMS:
- "Cardo" + "Packtalk", "Edge", "Pro", "mesh", "battery", "range", "pairing"
- "Sena" + "60X", "60S", "Spider", "Wave", "mesh", "warranty"
- "ASMAX" + "F1", "S1", "Hi Max", "mesh", "price", "value"
- "Reso" + "Pilot", "DuoSync", "camera", "range"

CRITICAL RULES:
1. ONLY REAL POSTS - Never fabricate customer feedback, posts, or URLs
2. Reddit only - do not include Facebook or Instagram content, that's handled elsewhere
3. Extract sentiment: positive, negative, mixed, or neutral
4. Include real product names (exact match with products[] in JSONs)
5. Summarize in 1-3 sentences (real words, no invention)
6. Include real URLs or null if not available
7. Do NOT duplicate existing posts (check dates)

OUTPUT FORMAT: Return JSON object with keys for each brand:
{
  "cardo": [
    {
      "date": "YYYY-MM-DD",
      "source": "Reddit",
      "forum": "r/motorcyclegear",
      "product": "exact product name or General",
      "sentiment": "positive|negative|mixed|neutral",
      "topic": "2-5 word label",
      "summary": "1-3 sentence real paraphrase",
      "url": "real URL or null"
    }
  ],
  "sena": [...],
  "asmax": [...],
  "reso": [...]
}

Return ONLY valid JSON with no markdown or explanation."""

    print("🔄 Calling Claude API for Social Media Listener...")

    full_response = ""
    with client.messages.stream(
        model="claude-opus-4-8",
        max_tokens=4000,
        messages=[{"role": "user", "content": prompt}]
    ) as stream:
        for text in stream.text_stream:
            full_response += text
            if len(full_response) % 500 == 0:
                print(".", end="", flush=True)

    print()

    # Parse JSON from response
    try:
        json_start = full_response.find('{')
        json_end = full_response.rfind('}') + 1
        if json_start >= 0 and json_end > json_start:
            json_str = full_response[json_start:json_end]
            feedback_data = json.loads(json_str)
            print("✅ Parsed social media feedback from Claude")
            return feedback_data
        else:
            print("⚠️ No JSON found in response, returning empty feedback")
            return {"cardo": [], "sena": [], "asmax": [], "reso": []}
    except json.JSONDecodeError as e:
        print(f"⚠️ Failed to parse feedback JSON: {e}")
        return {"cardo": [], "sena": [], "asmax": [], "reso": []}

def append_feedback_to_brands(feedback_data: dict) -> None:
    """Append new feedback to each brand's JSON."""
    for brand in ["cardo", "sena", "asmax", "reso"]:
        brand_json = load_brand_json(brand)
        new_feedback = feedback_data.get(brand, [])

        if not new_feedback:
            print(f"ℹ️  No new feedback found for {brand}")
            continue

        # Initialize customer_feedback array if missing
        if "customer_feedback" not in brand_json:
            brand_json["customer_feedback"] = []

        # Check for duplicates (by date + topic)
        existing_dates_topics = {
            (item.get("date"), item.get("topic"))
            for item in brand_json.get("customer_feedback", [])
        }

        added_count = 0
        for feedback_item in new_feedback:
            date_topic = (feedback_item.get("date"), feedback_item.get("topic"))
            if date_topic not in existing_dates_topics:
                brand_json["customer_feedback"].append(feedback_item)
                added_count += 1

        if added_count > 0:
            save_brand_json(brand, brand_json)
            print(f"✅ Added {added_count} new feedback entries to {brand}")
        else:
            print(f"ℹ️  No new feedback to add for {brand} (all duplicates)")

def main():
    print(f"\n{'='*60}")
    print("Social Media Listener Agent")
    print(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}")
    print(f"{'='*60}\n")

    try:
        # Gather feedback
        feedback_data = run_social_media_listener()

        # Append to brand JSONs
        append_feedback_to_brands(feedback_data)

        print("\n✅ Social Media Listener completed successfully")

    except Exception as e:
        print(f"\n❌ Error in Social Media Listener: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
