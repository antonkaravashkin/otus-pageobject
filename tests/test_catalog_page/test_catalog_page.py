from src.catalog.catalog_page import CatalogPage
import allure


class TestCatalogPage:
    @allure.title('Проверить элементы страницы каталог')
    def test_visibility_of_elements(self, tablets_catalog, driver):
        catalog = CatalogPage(driver)
        catalog.assert_compare_total_presence()
        catalog.assert_galaxy_img_presence()
        catalog.assert_sort_by_presence()
        catalog.assert_show_presence()
        catalog.assert_text_right_presence()
