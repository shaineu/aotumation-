import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def setup_playwright():
    print("starting playwright")

    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.ebay.com/")

    yield page

    # browser.close()
    # playwright.stop()