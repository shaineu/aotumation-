from playwright.sync_api import sync_playwright

from demoblaze_singin_test import user_name

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto( "https://demo.guru99.com/test/newtours/reservation.php")
    user_name.locator("userName")
    password=page.locator("password")
    lgoin_button = page.get_by_text("login")
    lgoin_button_by_name = page.locator("(name=loginbutton)")
    user_name.fill("standard user")
    password.fill("name=password")
lgoin_button_by_name.click()




