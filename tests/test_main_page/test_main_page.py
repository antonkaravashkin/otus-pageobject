from src.main_page.main_page import MainPage
import allure
import pytest

@pytest.mark.smoke
class TestMainPage:
    @allure.title('Проверить интерактивность Featured блока')
    def test_featured_product(self, driver):
        main_page = MainPage(driver)
        main_page.click_product_name(1)

    @allure.title('Проверить видимость карусели')
    def test_find_carousel(self, driver):
        main_page = MainPage(driver)
        main_page.assert_carousel_is_visible()

    @allure.title('Проверить видимость Свайпера')
    def test_check_swiper(self, driver):
        main_page = MainPage(driver)
        main_page.assert_swiper()
