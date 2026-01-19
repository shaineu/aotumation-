from playwright_expample.pom_swaglabs.pages.login_page import LoginPage
from playwright_expample.pom_swaglabs.pages.product_page import ProductPage


class TestProducts():


    def test_verify_first_price_is_less_than_50 (self, setup_playwright):
        page = setup_playwright
        LoginPage(page)
        ProductPage()
        page.goto("https://www.saucedemo.com/")
        LoginPage(page).set_user_and_password("standard_user" "secret_sauce")
        LoginPage(page).click_on_login()
        ProductPage().get_first_price()