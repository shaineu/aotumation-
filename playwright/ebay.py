from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://www.ebay.com/")
    page.wait_for_selector("#gh-ac")

    search_bar = page.locator("#gh-ac")
    search_bar.fill("shirt")
    search_bar.press("Enter")

    page.wait_for_load_state("networkidle")