class ResultPage:

    def __init__(self,page):
        self.page=page

    def lowest_price(self):
        self.page.wait_for_timeout(4000)
        self.page.get_by_text("Sort: Best Match", exact=False).click()
        self.page.get_by_text("Price + Shipping: lowest first", exact=False).click()
        self.page.keyboard.press("Enter")

    def choose_product(self, index):
        substring = f"#srp-river-results > ul > li:nth-child({index})"
        self.page.wait_for_timeout(4000)
        li_item = self.page.wait_for_selector(substring)
        target_span = li_item.wait_for_selector("div > div.su-card-container__content > div.su-card-container__attributes > div > div:nth-child(1) > span")
        price_text = target_span.inner_text()
        return price_text