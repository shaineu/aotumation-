class TestAdvantage:

    def test_contact_us(self, setup_playwright):
        page = setup_playwright

        page.goto("https://advantageonlineshopping.com/#/")

        # Go to Contact Us
        page.locator("text=CONTACT US").click()

        # Select category from list
        page.locator("select[name='categoryListboxContactUs']").select_option("Laptops")

        # Fill mandatory fields
        page.locator("input[name='emailContactUs']").fill("test@test.com")
        page.locator("textarea[name='subjectTextareaContactUs']").fill("QA Test")

        # Click Send
        page.locator("button:has-text('SEND')").click()

        # ASSERT – page still shows contact form
        assert page.locator("button:has-text('SEND')").is_visible()