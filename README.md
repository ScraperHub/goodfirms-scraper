# goodfirms-scraper

## Description

This repository contains Python-based scrapers for extracting company data from [GoodFirms](https://www.goodfirms.co/). These scrapers leverage the [Crawlbase Crawling API](https://crawlbase.com/crawling-api-avoid-captchas-blocks) to handle JavaScript rendering, CAPTCHA challenges, and anti-bot protections. The extracted data provides valuable insights into various businesses, including company names, locations, ratings, services, and profile details.

➡ Read the full blog [here](https://crawlbase.com/blog/how-to-scrape-goodfirms-data/) to learn more.

## Scrapers Overview

### GoodFirms Search Listings Scraper

The GoodFirms Search Listings Scraper (goodfirms_serp_scraper.py) extracts structured company information from search listings, including:

1. **Company Name**
2. **Location**
3. **Service Category**
4. **Rating**
5. **Company Profile URL**

It supports pagination, ensuring that multiple pages of search results can be scraped efficiently. Extracted data is stored in a structured JSON file.

### GoodFirms Company Profile Scraper

The GoodFirms Company Profile Scraper (goodfirms_company_page_scraper.py) extracts detailed company data from individual profile pages, including:

1. **Company Name**
2. **Description**
3. **Hourly Rate**
4. **Number of Employees**
5. **Year Founded**
6. **Services Offered**

It takes profile URLs from the search listings scraper and extracts detailed business information, saving the data in a JSON file.

## Environment Setup

Ensure that Python is installed on your system. Check the version using:

```bash
# Use python3 if you're on Linux/macOS
python --version
```

Install the required dependencies:

```bash
pip install crawlbase beautifulsoup4
```

- **Crawlbase** – Handles JavaScript rendering and bypasses bot protections.
- **BeautifulSoup** – Parses and extracts structured data from HTML.

## Running the Scrapers

1. **Get Your Crawlbase Access Token**

   - Sign up for Crawlbase [here](https://crawlbase.com/signup) to get an API token.
   - Replace `"YOUR_CRAWLBASE_TOKEN"` in the script with your Crawlbase Token.

2. **Run the Scraper**

```bash
# Use python3 if required (for Linux/macOS)
python SCRAPER_FILE_NAME.py
```

Replace `"SCRAPER_FILE_NAME.py"` with the actual script name (`goodfirms_serp_scraper.py` or `goodfirms_company_page_scraper.py`).

## To-Do List

- Extend scrapers to extract additional company details like contact information and portfolios.
- Optimize the scraping process for better performance.
- Implement multi-threading for large-scale data extraction.

## Why Use This Scraper?

- **Bypasses anti-bot protections** using Crawlbase.
- **Handles JavaScript-rendered content** efficiently.
- **Extracts structured company data** for business analysis.
