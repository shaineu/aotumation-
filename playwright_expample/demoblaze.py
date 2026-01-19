class TestDemoblaze:
    def test_demoblaze_correct_login(self,setup_playwright):
        print ("into test_demoblaze_correct_login")
        page = setup_playwright
        page.goto("https://www.demoblaze.com/")

    def test_go_to_cart(self, setup_playwright):
        page = setup_playwright
        page.goto("https://www.demoblaze.com/")