
import re

from ebay_project.pages.home_page import HomePage
from ebay_project.pages.result_page import ResultPage


class TestSearch:
    def test_search(self,setup_playwright):
        page = setup_playwright
        home_page =HomePage(page)
        home_page.search_for_item("shirt")
        home_page.search_button()
        result_page = ResultPage(page)
        result_page.lowest_price()
        first = result_page.choose_product(1)
        second = result_page.choose_product(2)
        third = result_page.choose_product(3)
        first = re.search(r'\d+(\.\d+)?', first) #regex from chatgpt
        first = float(float(first.group()))
        second = re.search(r'\d+(\.\d+)?', second)
        second = float(float(second.group()))
        third = re.search(r'\d+(\.\d+)?', third)
        third = float(float(third.group()))

        print("first: "+str(first))
        print("second: "+str(second))
        print("third: "+str(third))

        prices = [first, second, third]

        assert prices == sorted(prices), f"Prices are not ascending: {prices}"