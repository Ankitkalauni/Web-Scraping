import re
import requests
from bs4 import BeautifulSoup
from Books_to_scrape.locators.books_locator import BookLocators
from Books_to_scrape.parsers.book_parser import BookParser
from Quotes_to_scrape import locators
class BookParser:


    def __init__(self,parent):
        self.parent = parent
    @property
    def name(self):
        locator = BookLocators.NAME_LOCATOR
        item_link = self.parent.select_one(locator)
        item_name = item_link.attrs['title']
        return item_name

    @property
    def link(self):
        locator = BookLocators.LINK_LOCATOR
        item_link = self.parent.select_one(locator)
        link = item_link.attrs['href']
        return link


    @property
    def price(self):
        locator = BookLocators.PRICE_LOCATOR
        item_price = self.parent.select_one(locator).string

        pattern = '€([0-9]+\.[0-9]+)'
        matcher = re.search(pattern,item_price)

        return float(matcher.group(1))

    
    @property
    def rating(self):
        locator = BookLocators.RATING_LOCATOR
        item_rating = self.parent.select_one(locator)


