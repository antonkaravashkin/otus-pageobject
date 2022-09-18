from selenium.webdriver.common.by import By

from src.common_methods import CommonMethods


class ProductCard(CommonMethods):
    def __init__(self, driver):
        super().__init__(driver)

        self.add_to_cart = (By.XPATH, "//button[@id='button-cart']")
        self.reviews = (By.XPATH, "//a[contains(text(),'Reviews')]")
        self.review_input_name = (By.XPATH, "//input[@id='input-name']")
        self.review_review_field = (By.XPATH, "//textarea[@id='input-review']")
        self.five_star_rating = (
            By.XPATH,
            "//div[@class='col-sm-12']//input[@value='5']",
        )
        self.continue_button = (By.XPATH, "//button[@class='btn btn-primary']")

    def scroll_to_cart(self):
        element = self.find_element(*self.add_to_cart)
        self.scroll_element_into_center(element)

    def click_reviews_tab(self):
        self.find_element(*self.reviews).click()

    def click_continue_button(self):
        self.find_element(*self.continue_button).click()

    def fill_review_name(self, text):
        self.enter_credentials(*self.review_input_name, text)

    def fill_review(self, text):
        self.enter_credentials(*self.review_review_field, text)

    def click_five_star_rating(self):
        self.find_element(*self.five_star_rating).click()
