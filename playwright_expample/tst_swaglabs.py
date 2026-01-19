class TestSwaglabs:

    def test_swaglabs_correct_login(self,setup_playwright):
        print ("into test_swaglabs_correct_login")
        page = setup_playwright
        page.goto("https://www.saucedemo.com/")

        user = page.locator("#user-name")
        user.fill("standard_user")
        password = page.locator("#password")
        password.fill("secret_sauce")
        login_btn = page.get_by_text("login")
        login_btn.click()
        current_url = page.url
        assert current_url == "https://www.saucedemo.com/inventory.html", "current URL is not as expected"

    def test_swaglabs_incorrect_password_login(self, setup_playwright):
        print("into test_swaglabs_incorrect_login")
        page = setup_playwright
        page.goto("https://www.saucedemo.com/")

        user = page.locator("#user-name")
        user.fill("standard_user")
        password = page.locator("#password")
        password.fill("fake")
        login_btn = page.get_by_text("login")
        login_btn.click()
        current_url = page.url
        assert current_url == "https://www.saucedemo.com/", "current URL is not as expected"


    def test_swaglabs_incorrect_user_login(self, setup_playwright):
        print("into test_swaglabs_incorrect_login")
        page = setup_playwright
        page.goto("https://www.saucedemo.com/")
        user = page.locator("#user-name")
        user.fill("standard_user")
        password = page.locator("#password")
        password.fill("fake")
        login_btn = page.get_by_text("login")
        login_btn.click()
        current_url = page.url
        assert current_url == "https://www.saucedemo.com/", "current URL is not as expected"


    def test_swaglabs_get_first_price(self,setup_playwright):
        print ("into test_swaglabs_correct_login")
        page = setup_playwright
        page.goto("https://www.saucedemo.com/")

        user = page.locator("#user-name")
        user.fill("standard_user")
        password = page.locator("#password")
        password.fill("secret_sauce")
        login_btn = page.get_by_text("login")
        login_btn.click()
        list_prices = page.query_selector_all("[class='inventory_item_price']")
        first_price = list_prices[0]
        print (first_price.inner_text())

        print ("test end")

        def test_swaglabs_by_class(self, setup_playwright):
            page = setup_playwright
            page.goto("https://www.saucedemo.com/")
            # only in calss in case of space - sometimes it can be replaced by "."
            # e,g input_error.form_input.error instead of input_error form_input error
            elements = page.query_selector_all("[class*='input_error']")
            user = elements[0]
            password = elements[1]
            user.fill("standard_user")
            password.fill("secret_sauce")
            login_btn = page.get_by_text("login")
            login_btn.click()
            assert page.url == "https://www.saucedemo.com/inventory.html", "curren"