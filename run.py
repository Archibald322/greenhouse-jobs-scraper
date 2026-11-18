"""
Apify Client Runner for Greenhouse ATS Tech Jobs & Career Feeds Scraper
Actor URL: https://apify.com/moneygain/greenhouse-jobs-scraper
"""

import os
from apify_client import ApifyClient

api_token = os.getenv("APIFY_TOKEN", "YOUR_APIFY_TOKEN")
client = ApifyClient(api_token)

run_input = {
    "companies": ["figma", "stripe", "databricks"],
    "department": "",
    "location": "",
    "onlyRemote": False,
    "maxItems": 10
}

def main():
    print("🚀 Starting Greenhouse ATS Tech Jobs & Career Feeds Scraper on Apify Cloud...")
    run = client.actor("moneygain/greenhouse-jobs-scraper").call(run_input=run_input)
    print(f"✅ Scraping completed! Run ID: {run.get('id')}")
    
    dataset_client = client.dataset(run["defaultDatasetId"])
    items = list(dataset_client.iterate_items())
    print(f"📊 Retrieved {len(items)} records.")
    for item in items[:5]:
        print(f"-> [{item.get('company')}] {item.get('title')} | Apply: {item.get('jobUrl')}")

if __name__ == "__main__":
    main()
