from bs4 import BeautifulSoup
import json
from crawlbase import CrawlingAPI

# Initialize Crawlbase API with your access token
crawling_api = CrawlingAPI({'token': 'YOUR_CRAWLBASE_TOKEN'})

def make_crawlbase_request(url):
    response = crawling_api.get(url)

    if response['headers']['pc_status'] == '200':
        html_content = response['body'].decode('utf-8')
        return html_content
    else:
        print(f"Failed to fetch the page. Crawlbase status code: {response['headers']['pc_status']}")
        return None

def extract_company_details(company):
    name = company.select_one('h3.firm-name').text.strip() if company.select_one('h3.firm-name') else ''
    location = company.select_one('div.firm-location').text.strip() if company.select_one('div.firm-location') else ''
    category = company.select_one('div.firm-content > div.tagline').text.strip() if company.select_one('div.firm-content > div.tagline') else ''
    rating = company.select_one('span.rating-number').text.strip() if company.select_one('span.rating-number') else 'No rating'
    link = company.select_one('div.firm-urls > a.visit-profile')['href'] if company.select_one('div.firm-urls > a.visit-profile') else ''

    return {
        'name': name,
        'location': location,
        'category': category,
        'rating': rating,
        'profile_url': link
    }

def scrape_goodfirms_search_listings(url):
    html_content = make_crawlbase_request(url)
    if not html_content:
        return []

    soup = BeautifulSoup(html_content, 'html.parser')
    companies = soup.select('ul.firm-directory-list > li.firm-wrapper')
    company_data = []

    for company in companies:
        details = extract_company_details(company)
        company_data.append(details)

    return company_data

def scrape_all_pages(base_url, num_pages=5):
    all_data = []

    for page in range(1, num_pages + 1):
        url = f"{base_url}?page={page}"
        print(f"Scraping page {page}...")
        data = scrape_goodfirms_search_listings(url)
        all_data.extend(data)

    return all_data

def save_data_to_json(data, filename='goodfirms_search_data.json'):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)
    print(f"Data saved to {filename}")

# Example usage
base_url = "https://www.goodfirms.co/companies/web-development-agency/london"
all_data = scrape_all_pages(base_url, num_pages=5)
save_data_to_json(all_data)