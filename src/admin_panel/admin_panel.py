import time
import allure
from selenium.webdriver.common.by import By

from src.common_methods import CommonMethods


class AdminPanel(CommonMethods):
    def __init__(self, driver):
        super().__init__(driver)
        """Аналогично предыдущему заданию admin панель вызываем через аргумент --url терминала\командной строки"""
        self.panel_heading = (By.XPATH, "//div[@class='panel-heading']")
        self.username_label = (By.XPATH, "//label[text()='Username']")
        self.password_label = (By.XPATH, "//label[text()='Password']")
        self.footer = (By.XPATH, "//footer[@id='footer']")
        self.footer_opencart_link = (By.XPATH, "//a[text()='OpenCart']")
        self.login_button = (By.XPATH, "//button[@class='btn btn-primary']")
        self.username_field = (By.XPATH, "//input[@id='input-username']")
        self.password_field = (By.XPATH, "//input[@id='input-password']")
        self.menu_catalog = (By.XPATH, "//a[text()=' Catalog']")
        self.products = (By.XPATH, "//a[text()='Products']")
        self.save_button = (By.XPATH, "//button[@data-original-title='Save']")
        self.product_name = (By.XPATH, "//input[@id='input-name1']")
        self.meta_tag = (By.XPATH, "//input[@id='input-meta-title1']")
        self.data_tab = (By.XPATH, "//a[text()='Data']")
        self.general_tab = (By.XPATH, "//a[text()='General']")
        self.model = (By.XPATH, "//input[@id='input-model']")
        self.new_product = (By.XPATH, "//a[@data-original-title='Add New']")
        self.table = (By.XPATH, "//tbody")
        self.desirable_checkbox = (
            By.XPATH, "//tbody//tr//td[text()='Lopata']/..//input[@type='checkbox']")
        self.delete_button = (By.XPATH, "//button[@class='btn btn-danger']")
        self.deleted_element = (By.XPATH, "//tbody//tr//td[text()='Lopata']")
        self.filter_model = (By.XPATH, "//input[@id='input-model']")
        self.filter_button = (By.XPATH, "//button[@id='button-filter']")
        self.empty_table_body = (By.XPATH, "//tbody")

    @allure.step
    def click_footer_opencart_link(self):
        self.find_element(*self.footer_opencart_link).click()

    @allure.step
    def click_catalog(self):
        self.find_element(*self.menu_catalog).click()

    @allure.step
    def click_product(self):
        self.find_element(*self.products).click()

    @allure.step
    def click_data_tab(self):
        self.find_element(*self.data_tab).click()

    @allure.step
    def input_product_name(self, name: str):
        self.enter_credentials(*self.product_name, name)

    @allure.step
    def input_meta_tag(self, tag_name: str):
        self.enter_credentials(*self.meta_tag, tag_name)

    @allure.step
    def input_model(self, model_name: str):
        self.enter_credentials(*self.model, model_name)

    @allure.step
    def click_login_button(self):
        self.find_element(*self.login_button).click()

    @allure.step
    def click_save_button(self):
        self.find_element(*self.save_button).click()

    @allure.step
    def click_new_product(self):
        self.find_element(*self.new_product).click()

    @allure.step
    def click_general_tab(self):
        self.find_element(*self.general_tab).click()

    @allure.step
    def click_delete_button(self):
        self.find_element(*self.delete_button).click()
        time.sleep(2)

    @allure.step
    def click_filter_button(self):
        self.find_element(*self.filter_button).click()

    @allure.step
    def check_product_for_delete(self):
        """Условлюсь, что у меня конкретное наименование создаваемого товара"""
        elements = self.find_elements(*self.desirable_checkbox)
        self.logger.info(f"Отмечаем чек-боксы")
        if len(elements) >= 1:
            for element in elements:
                element.click()
                elements.pop(0)

    @allure.step
    def input_filter_model(self, text: str):
        self.enter_credentials(*self.filter_model, text)

    @allure.step
    def assert_created_product_exist(self):
        assert self.assert_element_visible(*self.deleted_element)

    @allure.step
    def input_name(self, login: str):
        self.enter_credentials(*self.username_field, login)

    @allure.step
    def input_password(self, password: str):
        self.enter_credentials(*self.password_field, password)

    @allure.step
    def assert_panel_header_visible(self):
        self.assert_element_visible(*self.panel_heading)

    @allure.step
    def assert_username_label_visible(self):
        self.assert_element_visible(*self.username_label)

    @allure.step
    def assert_password_label_visible(self):
        self.assert_element_visible(*self.password_label)

    @allure.step
    def assert_footer_text(self, title: str, pause: int = 1):
        time.sleep(pause)
        self.assert_text_equal(text=title, *self.footer)

    @allure.step
    def assert_no_filter_result(self, option):
        self.assert_text_equal(*self.empty_table_body, option)
