import sys
sys.path.append('/home/ankit/Desktop/git/Web-Scraping/Quotes_to_scrape/')

from locators.quote_locators import QuoteLocators

class QuoteParser:
    '''
    Given a specific a single div. get the information about the author, tag and description.
    '''


    def __init__(self,parent):
        self.parent = parent
    
    @property
    def content(self):
        locator = QuoteLocators.CONTENT

        return self.parent.select_one(locator).string

    @property
    def author(self):
        locator = QuoteLocators.AUTHOR

        return self.parent.select_one(locator).string

    @property
    def tags(self):
        locator = QuoteLocators.TAGS

        return self.parent.select_one(locator).string

    def __repr__(self):
        return f'Quote: {self.content} by {self.author}'