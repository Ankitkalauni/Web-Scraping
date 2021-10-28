import requests
import sys
sys.path.append('/home/ankit/Desktop/git/Web-Scraping/Quotes_to_scrape/')
from pages.quote_page import QuotesPage

page_content  = requests.get('http://quotes.toscrape.com').content
page = QuotesPage(page_content)

for quote in page.quotes:
    print(quote.tags)