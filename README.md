# Greenhouse ATS Tech Jobs & Career Feeds Scraper

[![Apify Actor](https://img.shields.io/badge/Apify-Actor%20Store-orange?logo=apify)](https://apify.com/moneygain/greenhouse-jobs-scraper)
[![Python Version](https://img.shields.io/badge/Python-3.10%20%7C%203.11%20%7C%203.12-blue?logo=python)](https://github.com/Archibald322/greenhouse-jobs-scraper)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> **Live Apify Store Actor:** [https://apify.com/moneygain/greenhouse-jobs-scraper](https://apify.com/moneygain/greenhouse-jobs-scraper)

This repository provides an open-source Python runner and documentation for **[Greenhouse ATS Tech Jobs & Career Feeds Scraper](https://apify.com/moneygain/greenhouse-jobs-scraper)**.

---

## ⚡ Quickstart

### Option 1: Run in Cloud (No Code)
Launch directly from your browser via the Apify Store console:
👉 **[Open Greenhouse ATS Tech Jobs & Career Feeds Scraper on Apify Store](https://apify.com/moneygain/greenhouse-jobs-scraper)**

### Option 2: Run via Python SDK
```bash
git clone https://github.com/Archibald322/greenhouse-jobs-scraper.git
cd greenhouse-jobs-scraper
pip install -r requirements.txt
export APIFY_TOKEN="your_apify_token_here"
python run.py
```

---

# 🚀 Greenhouse ATS Tech Jobs & Career Feeds Scraper

**Scrape Greenhouse ATS job postings to JSON, CSV, or Excel in seconds without browser overhead.** Extract verified job openings, job titles, departments, offices, locations, remote status, requisition tracking IDs, updated timestamps, clean plain-text descriptions, and direct apply links from **boards.greenhouse.io** — the world's most popular applicant tracking system powering hiring for Figma, Stripe, Databricks, Airbnb, DoorDash, Pinterest, Gitlab, Roblox, Instacart, Discord, and thousands of top global tech leaders.

Designed for AI talent agents, recruitment automation teams, headhunters, B2B sales intelligence platforms (tracking hiring signals), and market researchers. Powered by direct lightweight HTTP requests with **zero browser overhead** and **100% Pay-Per-Event (PPE) pricing** — you only pay for verified job records delivered ($0.005 / job posting).

---

## ⚡ Speed & Value Comparison

| Feature | Our Lightweight Greenhouse Scraper | Heavy Browser Scrapers (Playwright / Puppeteer) |
|---|---|---|
| **Memory Consumption** | **128 MB – 256 MB** | 2 GB – 4 GB |
| **Startup Cost** | **$0.00 (Zero Start Fee)** | $0.05 – $0.10 per run |
| **Extraction Speed** | **0.15s – 0.3s per company board** | 10s – 25s per page |
| **Pricing Model** | **Pay-Per-Event ($0.005 / job record)** | Expensive Monthly Flat Rate ($30–$50/mo) |
| **Data Enrichment** | **Clean plain-text descriptions + remote detection** | Raw HTML tags requiring complex post-processing |
| **AI & MCP Ready** | **Instant clean JSON for Claude / Cursor MCP** | Bulky payloads requiring heavy LLM cleanup |

---

## 📦 Sample JSON Output

```json
{
  "id": "5426468004",
  "title": "Account Executive, Enterprise",
  "company": "Figma",
  "companyToken": "figma",
  "jobUrl": "https://boards.greenhouse.io/figma/jobs/5426468004?gh_jid=5426468004",
  "location": "San Francisco, CA • New York, NY • United States",
  "isRemote": false,
  "departments": [
    "Sales"
  ],
  "offices": [
    "US"
  ],
  "updatedAt": "2026-10-27T13:40:12-04:00",
  "requisitionId": "1451",
  "plainTextDescription": "Figma is growing our team of passionate creatives and builders on a mission to make design accessible to all. Figma’s platform connects anyone involved in the digital product design process, from ideation to production. We are looking for an experienced Enterprise Account Executive to join our team...",
  "htmlDescription": "<div class=\"content-intro\"><p>Figma is growing our team of passionate creatives and builders on a mission to make design accessible to all.</p></div>..."
}
```

---

## 🤖 AI & No-Code Integrations

### Claude Desktop & Cursor IDE (Apify MCP Server)
Connect this scraper directly to your AI workflows using the official Apify Model Context Protocol (MCP) server. Run natural language research:
> *"Extract all open Software Engineering and AI Research roles from Stripe and Databricks on Greenhouse that offer remote options, and output their titles and apply URLs."*

```json
{
  "mcpServers": {
    "apify": {
      "command": "npx",
      "args": ["-y", "@apify/mcp-server"],
      "env": {
        "APIFY_TOKEN": "YOUR_APIFY_TOKEN"
      }
    }
  }
}
```

### Python SDK Quickstart
```python
from apify_client import ApifyClient

client = ApifyClient("YOUR_APIFY_TOKEN")
run_input = {
    "companies": ["figma", "stripe", "databricks"],
    "department": "Engineering",
    "onlyRemote": True,
    "maxItems": 25
}

run = client.actor("moneygain/greenhouse-jobs-scraper").call(run_input=run_input)
for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(f"[{item['company']}] {item['title']} -> {item['jobUrl']}")
```

### n8n / Make.com / Clay Integration
1. Add an **Apify** node to your scenario.
2. Select **Run Actor** and enter `moneygain/greenhouse-jobs-scraper`.
3. Map the dataset records to your Google Sheets, Airtable, CRM (HubSpot, Salesforce), or outbound recruitment outreach sequence.

---

## ⚙️ Input Parameters

| Parameter | Type | Default | Description |
|---|---|---|---|
| `companies` | Array of Strings | `["figma", "stripe", "databricks"]` | List of company tokens or direct Greenhouse board URLs (e.g. `figma`, `https://boards.greenhouse.io/airbnb`). |
| `department` | String | `""` | Optional department filter (e.g. `Engineering`, `Product`, `Design`, `Sales`). |
| `location` | String | `""` | Optional location filter (e.g. `San Francisco`, `New York`, `Remote`, `London`). |
| `onlyRemote` | Boolean | `false` | When true, filters strictly for positions flagged as remote, distributed, or anywhere. |
| `maxItems` | Integer | `10` | Maximum number of job postings to extract. Default is 10 for instant 5-second testing. |

---

## ❓ Frequently Asked Questions (FAQ)

### 1. Is it legal to scrape Greenhouse job postings?
Yes. All job records retrieved by this scraper are publicly published by hiring companies on their official open Greenhouse job boards (`boards.greenhouse.io`). Our scraper extracts only public factual job listings in compliance with GDPR and fair-use data aggregation standards.

### 2. How do I find a company's Greenhouse token?
The company token is the slug at the end of their Greenhouse career page URL. For example, if the career board is `https://boards.greenhouse.io/figma`, the token is simply `figma`. You can paste either the bare token or the full board URL directly into the `companies` input.

### 3. How much does it cost to extract 1,000 jobs?
With our **Pay-Per-Event ($0.005 / job record)** pricing model, extracting 1,000 verified job postings costs exactly **$5.00** (with automatic volume discounts down to $4.00/1k). There are no compute unit (CU) markups, no proxy fees, and zero hidden costs.

### 4. Can I export Greenhouse job data to Excel or CSV?
Yes. From the Apify Console or API, you can export your scraped datasets in one click into CSV, Excel, JSON, XML, or RSS formats.

### 5. Why is this scraper faster than browser-based scrapers?
Traditional scrapers launch heavy headless browsers (Chrome/Puppeteer) that consume 2 GB to 4 GB of RAM and load megabytes of redundant styles, fonts, and tracking scripts. Our scraper queries the underlying optimized Greenhouse board REST API directly, returning clean structured JSON in less than 0.2 seconds on just 128 MB of memory.

---

## 🔗 Explore More High-Speed B2B Scrapers & Enrichers by Our Team

| Scraper | Data Source | Primary Use Case | Store Link |
|---|---|---|---|
| **Y Combinator Startups Scraper** | YCombinator.com | Verified YC startups, founders, batches & hiring status | [Run on Apify](https://apify.com/moneygain/ycombinator-startups-scraper) |
| **TrustMRR Startups Scraper** | TrustMRR.com | Stripe-verified SaaS MRR, revenue & founder handles | [Run on Apify](https://apify.com/moneygain/trustmrr-startups-scraper) |
| **Ashby ATS Jobs Scraper** | AshbyHQ.com | High-growth tech vacancies & compensation | [Run on Apify](https://apify.com/moneygain/ashby-jobs-scraper) |
| **Clutch B2B Agencies Scraper** | Clutch.co | Top IT agencies, hourly rates & client reviews | [Run on Apify](https://apify.com/moneygain/clutch-agencies-scraper) |
| **Wellfound Jobs Scraper** | Wellfound.com | Startup equity benchmarks, tech talent & YC jobs | [Run on Apify](https://apify.com/moneygain/wellfound-jobs-scraper) |
| **TheProtocol.it Scraper** | TheProtocol.it | European IT salaries & tech stack benchmarks | [Run on Apify](https://apify.com/moneygain/theprotocol-scraper) |
| **Bulldogjob Scraper** | Bulldogjob.pl | Developer hiring trends & B2B compensation | [Run on Apify](https://apify.com/moneygain/bulldogjob-scraper) |
