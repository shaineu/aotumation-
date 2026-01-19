class HomePage():

    def __init__(self, page):
        self.page = page

    def home_page(self):
         self.page.goto("https://yahoo.com")
    def click_on_finance(self):
        self.page.self.page.get_by_role("link", name="Finance")
