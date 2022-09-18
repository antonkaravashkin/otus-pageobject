import time
import logging
import allure
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec


class CoreMethods:
    def __init__(self, driver):
        self.driver = driver

        self.logger = logging.getLogger(type(self).__name__)
        file = logging.FileHandler(f"logs/{self.driver.test_name}.log")
        file.setFormatter(logging.Formatter(
            "%(asctime)s - %(name)s - %(message)s"))
        self.logger.addHandler(file)
        self.logger.setLevel(self.driver.log_level)

    def get_element(self, by: By, value: str, timeout: int = 5):
        return self.find_element(by, value, timeout)

    def find_element_by_text(self, text):
        self.logger.info(f"Находим элемент по тексту {text}")
        return self.find_element(By.XPATH, f"//*[text()='{text}']")

    def find_element(self, by: By, value: str, timeout: int = 5):
        """Ключевой метод с ожиданием"""
        try:
            self.logger.info(f"Найден элемент {value}")
            return WebDriverWait(self.driver, timeout).until(
                ec.visibility_of_element_located((by, value))
            )
        except:
            self.logger.warning(f"Не нашелся элемент {value}")
            allure.attach(body=self.driver.get_screenshot_as_png(),
                          name="screenshot_image", attachment_type=allure.attachment_type.PNG)

    def find_elements(self, by: By, value: str, timeout: int = 5):
        self.logger.info(f"Находим список элементов {value}")
        return WebDriverWait(self.driver, timeout).until(
            ec.visibility_of_all_elements_located((by, value))
        )

    def select_drop_option(self, text):
        element = self.find_element_by_text(text=text)
        self.logger.info(f"Кликаем в элемент {text}")
        element.click()

    def scroll_element_into_center(self, element: WebElement):
        self.logger.info(f"Скроллим страницу до <{element.text}>")
        self.driver.execute_script(
            'arguments[0].scrollIntoView({block: "center"});', element
        )
        time.sleep(1)

    def enter_credentials(self, by: By, value: str, option: str):
        element = self.get_element(by, value)
        self.logger.info(f"Вводим {option} в поле {value}")
        element.click()
        element.clear()
        element.send_keys(option)

    def dissmiss_alert(self):
        self.logger.info(f"Алерт - отказать")
        self.driver.switch_to.alert.dismiss()

    def accept_alert(self):
        self.logger.info(f"Алерт - Принять")
        self.driver.switch_to.alert.accept()

    def assert_element_visible(self, by: By, value: str, timeout: int = 5):
        try:
            self.logger.info(f"Пытаемся найти элемент {value}")
            self.find_element(by, value, timeout)
            return True
        except TimeoutException:
            self.logger.info(f"Не смогли найти элемент {value}")
            allure.attach(body=self.driver.get_screenshot_as_png(),
                          name="screenshot_image", attachment_type=allure.attachment_type.PNG
                          )
            return False

    def assert_text_equal(self, by: By, value: str, text: str):
        text_element = self.find_element(by, value).text.strip()
        try:
            self.logger.info(f"Сравниваем {text_element} с {text}")
            assert text_element == text
        except:
            self.logger.warning(f"Ожидался {text}, получен {text_element}")
            allure.attach(body=self.driver.get_screenshot_as_png(),
                          name="screenshot_image", attachment_type=allure.attachment_type.PNG)

    def assert_current_url(self, url: str):
        current_url = self.driver.current_url
        self.logger.info(f"Проверяем открытый {current_url}")
        assert current_url == url, self.logger.warning(
            f"Ожидался {url}, открылся {current_url}")
