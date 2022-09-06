import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec


class CoreMethods:
    def __init__(self, driver):
        self.driver = driver

    def get_element(self, by: By, value: str, timeout: int = 5):
        return self.find_element(by, value, timeout)

    def find_element_by_text(self, text):
        return self.find_element(By.XPATH, f"//*[text()='{text}']")

    def find_element(self, by: By, value: str, timeout: int = 5):
        """Ключевой метод с ожиданием"""
        return WebDriverWait(self.driver, timeout).until(
            ec.visibility_of_element_located((by, value))
        )

    def find_elements(self, by: By, value: str, timeout: int = 5):
        return WebDriverWait(self.driver, timeout).until(
            ec.visibility_of_all_elements_located((by, value))
        )

    def select_drop_option(self, text):
        element = self.find_element_by_text(text=text)
        element.click()

    def scroll_element_into_center(self, element: WebElement):
        self.driver.execute_script(
            'arguments[0].scrollIntoView({block: "center"});', element
        )
        time.sleep(1)

    def enter_credentials(self, by: By, value: str, option: str):
        element = self.get_element(by, value)
        element.click()
        element.clear()
        element.send_keys(option)
    
    def dissmiss_alert(self):
        self.driver.switch_to.alert.dismiss()

    def accept_alert(self):
        self.driver.switch_to.alert.accept()

    def assert_element_visible(self, by: By, value: str, timeout: int = 5):
        try:
            self.find_element(by, value, timeout)
            return True
        except TimeoutException:
            return False

    def assert_text_equal(self, by: By, value: str, text: str):
        text_element = self.find_element(by, value).text.strip()
        assert text_element == text, f"Ожидался {text_element}"

    def assert_current_url(self, url: str):
        current_url = self.driver.current_url
        assert current_url == url, f"Ожидался {url}, открылся {current_url}"
