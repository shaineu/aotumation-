from playwright.async_api import Playwright
class HomePage:
    def __init__(self, page):
      self.page = page
    def search_for_item(self,value):
        search_bar = self.page.wait_for_selector("#gh-ac")
        search_bar.fill(value)
    def search_button(self):
        search_button = self.page.wait_for_selector("#gh-search-btn")
        search_button.click()







