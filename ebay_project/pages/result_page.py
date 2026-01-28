class ResultPage:

    def __init__(self,page):
        self.page=page

    #//*[@id='s0-2-54-0-9-8-4-2-0-4[1]-74-51-1-@content-menu']/li[4]
    def lowest_price(self):
        self.page.get_by_text("Sort: Best Match", exact=False).click()
        self.page.wait_for_timeout(2000)  # 5 seconds
        self.page.get_by_text("Price + Shipping: lowest first", exact=False).click()
        self.page.keyboard.press("Enter")

#//*[@id="item2e093b8c47"]/div/div[2]/div[2]/div[1]/div[1]
    def choose_product(self,index):
        print('**********************************************************')
        self.page.wait_for_timeout(4000)  # 5 seconds
        price_of_product = self.page.locator("//*[@id='item2e093b8c47']/div/div[2]/div[2]/div[1]/div[1]")
        print(price_of_product.inner_text())
















