from src.common_methods import CommonMethods
from selenium.webdriver.common.by import By


class AboutUs(CommonMethods):
    def __init__(self, driver):
        super().__init__(driver)

        self.about_title = (By.XPATH, "//h1[text()='About Us']")

    def assert_about_title(self, option: str):
        self.assert_text_equal(*self.about_title, text=option)
