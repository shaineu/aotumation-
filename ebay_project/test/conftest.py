import pytest
import os
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def setup_playwright():

    playwright = sync_playwright().start()
    user_data_dir = os.path.join(os.getcwd(), "playwright_data")
    context = playwright.chromium.launch_persistent_context(
            user_data_dir,
            headless=False,
            args=[
                "--disable-blink-features=AutomationControlled",
                "--start-maximized"
            ]
        )
    page = context.pages[0]
    page.goto("https://www.ebay.com/",wait_until="networkidle")

    yield page

    page.close()
    # browser.close()