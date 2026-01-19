class TestGuru99:
    def test_guru99_login(self,setup_playwright):
        print ("into test_guru99_login")
        page = setup_playwright
        page.goto("https://demo.guru99.com/test/newtours/#google_vignette")
        user = page.locator("[name='userName']")
        user.fill("tutorial")
        password = page.locator("[name='password']")
        password.type("tutorial")
        submit = page.locator("[name='submit']")
        submit.click()

    def test_guru99_flight_search(self, setup_playwright):
        print("into test_guru99_flight_search")
        page = setup_playwright
        page.goto("https://demo.guru99.com/test/newtours/#google_vignette")
        page.get_by_role("link", name="Flights").click()
        page.locator("input[value='oneway']").click()
        passengers = page.locator("[name='passCount']")
        passengers.select_option("1")
        from_city = page.locator("[name='fromPort']")
        from_city.select_option("Paris")
        continue_btn = page.locator("[name='findFlights']")
        continue_btn.click()


        print("Flight search end")