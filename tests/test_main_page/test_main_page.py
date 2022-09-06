from src.main_page.main_page import MainPage


class TestMainPage:
    def test_featured_product(self, driver):
        main_page = MainPage(driver)
        main_page.click_product_name(1)

    def test_find_carousel(self, driver):
        main_page = MainPage(driver)
        main_page.assert_carousel_is_visible()

    def test_check_swiper(self, driver):
        main_page = MainPage(driver)
        main_page.assert_swiper()
