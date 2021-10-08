# importing sys
import sys
  
# adding Folder_2 to the system path
sys.path.insert(0, '/home/ankit/Desktop/git/Web-Scraping/Quotes_to_scrape')
sys.path.insert(0, '/home/ankit/Desktop/git/Web-Scraping/Quotes_to_scrape/locators')
sys.path.insert(0, '/home/ankit/Desktop/git/Web-Scraping/Quotes_to_scrape/parsers')

for c in sys.path:
    print(c)