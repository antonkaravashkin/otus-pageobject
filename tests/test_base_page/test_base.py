import allure
import pytest
from src.common_methods import CommonMethods
from src.about_us.about_us import AboutUs
from data.footer_data import ABOUTUS
from data.variables import TEST_URL


@pytest.mark.smoke
class TestOverall:
    @allure.title('Переход на страницу "О нас" через футер')
    def test_footer_aboutus_redirect(self, driver):
        footer = CommonMethods(driver)
        footer.click_footer_option(ABOUTUS)
        about = AboutUs(driver)
        about.assert_about_title(ABOUTUS)
        about.assert_current_url(TEST_URL + "/about_us")

    @allure.title('Проверить, что в футере есть выбор опций')
    def test_check_aboutus_footer(self, driver):
        footer = CommonMethods(driver)
        footer.assert_footer_information_option()
