from selenium.webdriver.common.by import By

from src.common_methods import CommonMethods


class RegistrationPage(CommonMethods):
    def __init__(self, driver):
        super().__init__(driver)

        self.personal_details = (By.XPATH, "//fieldset[@id='account']/legend")
        self.telephone = (By.XPATH, "//input[@id='input-telephone']")
        self.password_title = (By.XPATH, "//legend[text()='Your Password']")
        self.newsletter = (By.XPATH, "//legend[text()='Newsletter']")
        self.subscribe = (By.XPATH, "//label[text()='Subscribe']")

        self.first_name = (By.XPATH, "//input[@id='input-firstname']")
        self.last_name = (By.XPATH, "//input[@id='input-lastname']")
        self.e_mail = (By.XPATH, "//input[@id='input-email']")
        self.telephone_field = (By.XPATH, "//input[@id='input-telephone']")
        self.password_field = (By.XPATH, "//input[@id='input-password']")
        self.confirm_password = (By.XPATH, "//input[@id='input-confirm']")
        self.privecy_policy = (By.XPATH, "//input[@name='agree']")
        self.account_creation_text = (By.XPATH, "//div[@id='content']//h1")
        self.submit_button = (By.XPATH, "//input[@type='submit']")

        self.checkbox = (By.XPATH, "//input[@name='agree']")


    def input_first_name(self, options):
        self.enter_credentials(*self.first_name, options)

    def input_last_name(self, options):
        self.enter_credentials(*self.last_name, options)
    
    def input_email(self, options):
        self.enter_credentials(*self.e_mail, options)
    
    def input_telephone(self, options):
        self.enter_credentials(*self.telephone_field, options)

    def input_password(self, options):
        self.enter_credentials(*self.password_field, options)
    
    def input_password_confirmation(self, options):
        self.enter_credentials(*self.confirm_password, options)

    def click_privacy_checkbox(self):
        self.find_element(*self.privecy_policy).click()
        self.logger.info(f"Отмечаем чек-бокс")

    def submit_form(self):
        self.find_element(*self.submit_button).submit()
        self.logger.info(f"Нажимаем кнопку Submit")

    def assert_personal_details(self):
        assert self.assert_element_visible(*self.personal_details)

    def assert_telephone_field(self):
        assert self.assert_element_visible(*self.telephone)

    def assert_password_title(self):
        assert self.assert_element_visible(*self.password_title)

    def assert_newsletter(self):
        assert self.assert_element_visible(*self.newsletter)

    def assert_subscribe_block(self):
        assert self.assert_element_visible(*self.subscribe)

    def assert_account_creation_text(self, option):
        assert self.assert_text_equal(*self.account_creation_text, option)
