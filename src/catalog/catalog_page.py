import allure
from selenium.webdriver.common.by import By

from src.common_methods import CommonMethods


class CatalogPage(CommonMethods):
    def __init__(self, driver):
        super().__init__(driver)

        self.compare_total = (By.XPATH, "//a[@id='compare-total']")
        self.galaxy_tab = (By.XPATH, "//img[@title='Samsung Galaxy Tab 10.1']")
        self.sort_by = (By.XPATH, "//div[@class='col-md-4 col-xs-6']")
        self.show = (By.XPATH, "//div[@class='col-md-3 col-xs-6']")
        self.text_right = (By.XPATH, "//div[@class='col-sm-6 text-right']")

    @allure.step
    def assert_compare_total_presence(self):
        assert self.assert_element_visible(*self.compare_total)

    @allure.step
    def assert_galaxy_img_presence(self):
        assert self.assert_element_visible(*self.galaxy_tab)

    @allure.step
    def assert_sort_by_presence(self):
        assert self.assert_element_visible(*self.sort_by)

    @allure.step
    def assert_show_presence(self):
        assert self.assert_element_visible(*self.show)

    @allure.step
    def assert_text_right_presence(self):
        assert self.assert_element_visible(*self.text_right)

    @allure.step
    def click_product_card(self, text):
        self.find_element_by_text(text).click()
