from bs4 import BeautifulSoup
from Books_to_scrape.locators.all_books import AllBookLocators
from Books_to_scrape.parsers.book_parser import BookParser

class AllBookPage:
    def __init__(self,page):
        self.soup = BeautifulSoup(page, 'html.parser')

    @property
    def books(self):
        return [BookParser(e) for e in self.soup.select(AllBookLocators.BOOKS)]