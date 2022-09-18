import allure
from selenium.webdriver.common.by import By

from src.common_methods import CommonMethods


class MainPage(CommonMethods):
    def __init__(self, driver):
        super().__init__(driver)

        self.featured = (By.CSS_SELECTOR, "#content > div.row .product-layout")
        self.product_name = (By.XPATH, "//div[@class='caption']/h4/a")
        self.carousel = (By.XPATH, "//div[@class='carousel swiper-viewport']")
        self.main_page_swiper = (By.XPATH, "//div[@id='slideshow0']")

    @allure.step
    def click_product_name(self, index):
        self.find_elements(*self.product_name)[index].click()

    @allure.step
    def assert_carousel_is_visible(self):
        element = self.find_element(*self.carousel)
        self.scroll_element_into_center(element)
        assert self.assert_element_visible(*self.carousel)

    @allure.step
    def assert_swiper(self):
        assert self.assert_element_visible(*self.main_page_swiper)
