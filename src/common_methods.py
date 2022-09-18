import allure
from selenium.webdriver.common.by import By
from src.core_methods import CoreMethods


class CommonMethods(CoreMethods):
    def __init__(self, driver):
        """Здесь собраны элементы и методы с повсеместно встречающимися на страницах"""
        super().__init__(driver)

        self.open_cart_logo = (By.CSS_SELECTOR, "img[title='Your Store']")
        self.title = (By.XPATH, "//div[@id='content']/h2")
        self.navigation_bar = (By.CSS_SELECTOR, ".navbar-header")
        self.desktop = (
            By.XPATH, "//li[@class='dropdown']/a[text()='Desktops']")
        self.laptops = (
            By.XPATH,
            "//li[@class='dropdown']/a[text()='Laptops & Notebooks']",
        )
        self.components = (
            By.XPATH, "//li[@class='dropdown']/a[text()='Components']")
        self.tablets = (By.XPATH, "//a[text()='Tablets']")
        self.software = (By.XPATH, "//a[text()='Software']")
        self.phones = (By.XPATH, "//a[text()='Phones & PDAs']")
        self.cameras = (By.XPATH, "//a[text()='Cameras']")
        self.players = (By.XPATH, "//a[text()='MP3 Players']")
        self.search_field = (
            By.XPATH, "//input[@class='form-control input-lg']")
        self.search_button = (
            By.XPATH, "//button[@class='btn btn-default btn-lg']")
        self.search_title = (By.XPATH, "//div[@id='content']/h1")
        self.swiper = (By.XPATH, "//div[@id='slideshow0']")
        self.inactive_bullet = (
            By.XPATH, "//span[@class='swiper-pagination-bullet']")
        self.active_bullet = (
            By.XPATH,
            "//span[@class='swiper-pagination-bullet swiper-pagination-bullet-active']",
        )
        self.phone_icon = (By.XPATH, "//i[@class='fa fa-phone']")
        self.phone_number = (By.XPATH, "//ul[@class='list-inline']/li[1]/span")
        self.featured = (By.XPATH, "//div[@id='content']//h3")
        self.cinema = (By.XPATH, '//a[contains(text(),"Apple Cinema 30")]')
        self.my_account = (
            By.XPATH, "//div[@id='top-links']//li[@class='dropdown']")
        self.wish_list = (By.XPATH, "//a[@id='wishlist-total']")
        self.shopping_cart = (By.XPATH, "//a[@title='Shopping Cart']")
        self.checkout = (By.XPATH, "//a[@title='Checkout']")
        self.shopping_cart_big = (By.XPATH, "//div[@id='cart']")
        self.currency_tab = (
            By.XPATH,
            "//button[@class='btn btn-link dropdown-toggle']",
        )
        self.footer_information = (By.XPATH, "//h5[text()='Information']")
        self.footer_aboutus = (
            By.XPATH,
            "//h5[text()='Information']/..//a[text()='About Us']",
        )
        self.footer_delivey = (
            By.XPATH,
            "//h5[text()='Information']/..//a[text()='Delivery Information']",
        )
        self.footer_privacy = (
            By.XPATH,
            "//h5[text()='Information']/..//a[text()='Privacy Policy']",
        )
        self.footer_terms = (
            By.XPATH,
            "//h5[text()='Information']/..//a[text()='Terms & Conditions']",
        )

    @allure.step
    def click_currency_dropdown(self):
        self.find_element(*self.currency_tab).click()

    @allure.step
    def click_phone_button(self):
        self.find_element(*self.phone_icon).click()

    @allure.step
    def click_my_account_button(self):
        self.find_element(*self.my_account).click()

    @allure.step
    def click_navbar_wishlist_button(self):
        self.find_element(*self.wish_list).click()

    @allure.step
    def click_shoppingcart_button(self):
        self.find_element(*self.shopping_cart).click()

    @allure.step
    def click_checkout_button(self):
        self.find_element(*self.checkout).click()

    @allure.step
    def input_search(self, option):
        self.enter_credentials(*self.search_field, option)

    @allure.step
    def search_button_click(self):
        self.find_element(*self.search_button).click()

    @allure.step
    def open_catalog_with_single_section(self, text):
        self.find_element_by_text(text=text).click()

    @allure.step
    def assert_currency_mark(self, option):
        self.assert_text_equal(*self.currency_tab, option)

    @allure.step
    def assert_footer_information_option(self):
        elements = (
            self.footer_aboutus,
            self.footer_delivey,
            self.footer_privacy,
            self.footer_terms,
        )
        locator = self.find_element(*self.footer_information)
        self.scroll_element_into_center(locator)
        for element in elements:
            assert self.assert_element_visible(
                *element
            ), f"Не нашелся элемент {element[1]}"


    @allure.step
    def click_footer_option(self, option: str):
        self.find_element_by_text(text=option).click()
