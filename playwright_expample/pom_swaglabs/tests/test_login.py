from playwright_expample.pom_swaglabs.pages.login_page import LoginPage
class TestLogin():

    def test_contact_us(self, setup_playwright):

        page = setup_playwright
        LoginPage(page)
        page.goto("https://www.saucedemo.com/")