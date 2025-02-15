from bs4 import BeautifulSoup
import json
from crawlbase import CrawlingAPI
import re

# Initialize Crawlbase API with your access token
crawling_api = CrawlingAPI({'token': 'YOUR_CRAWLBASE_TOKEN'})

def make_crawlbase_request(url):
    """Fetch the HTML content of a page using Crawlbase."""
    response = crawling_api.get(url)

    if response['headers']['pc_status'] == '200':
        html_content = response['body'].decode('utf-8')
        return html_content
    else:
        print(f"Failed to fetch the page. Crawlbase status code: {response['headers']['pc_status']}")
        return None

def extract_profile_details(html_content):
    """Extract detailed information from a company profile page."""
    soup = BeautifulSoup(html_content, 'html.parser')

    name = soup.select_one('h1[itemprop="name"]').text.strip() if soup.select_one('h1[itemprop="name"]') else 'N/A'
    description = re.sub(r'\s+', ' ', soup.select_one('div.profile-summary-text').text.strip()) if soup.select_one('div.profile-summary-text') else 'N/A'
    hourly_rate = soup.select_one('div.profile-pricing > span').text.strip() if soup.select_one('div.profile-pricing > span') else 'N/A'
    no_of_employees = soup.select_one('div.profile-employees > span').text.strip() if soup.select_one('div.profile-employees > span') else 'N/A'
    year_founded = soup.select_one('div.profile-founded > span').text.strip() if soup.select_one('div.profile-founded > span') else 'N/A'
    services = [item['data-name'] for item in soup.select('ul.services-chart-list button')]

    return {
        'name': name,
        'description': description,
        'hourly_rate': hourly_rate,
        'no_of_employees': no_of_employees,
        'year_founded': year_founded,
        'services': services
    }

def scrape_company_profiles(profile_urls):
    """Scrape multiple company profiles."""
    profiles_data = []

    for url in profile_urls:
        print(f"Scraping profile: {url}")
        html_content = make_crawlbase_request(url)
        if html_content:
            details = extract_profile_details(html_content)
            profiles_data.append(details)

    return profiles_data

def save_profiles_to_json(data, filename='goodfirms_profiles.json'):
    """Save company profile data to a JSON file."""
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)
    print(f"Profile data saved to {filename}")

# Example usage
profile_urls = [
    "https://www.goodfirms.co/company/unified-infotech",
    "https://www.goodfirms.co/company/sigli"
]

profiles_data = scrape_company_profiles(profile_urls)
save_profiles_to_json(profiles_data)