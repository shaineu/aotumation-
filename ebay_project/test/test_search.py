from ebay_project.pages.home_page import HomePage
from ebay_project.pages.result_page import ResultPage


class TestSearch:
    def test_search(self,setup_playwright):
        page = setup_playwright
        home_page =HomePage(page)
        home_page.search_for_item("shoes")
        home_page.search_button()
        result_page = ResultPage(page)
        result_page.lowest_price()
        result_page.choose_product(1)