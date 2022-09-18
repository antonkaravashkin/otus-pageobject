import allure
from src.common_methods import CommonMethods
from src.about_us.about_us import AboutUs
from data.footer_data import ABOUTUS
from data.variables import TEST_URL


class TestOverall:
    @allure.title('Footer about us redirect')
    def test_footer_aboutus_redirect(self, driver):
        footer = CommonMethods(driver)
        footer.click_footer_option(ABOUTUS)
        about = AboutUs(driver)
        about.assert_about_title(ABOUTUS)
        about.assert_current_url(TEST_URL + "/about_us")

    @allure.title('Footer information iption')
    def test_check_aboutus_footer(self, driver):
        footer = CommonMethods(driver)
        footer.assert_footer_information_option()
