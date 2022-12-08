from src.product_page.product_card import ProductCard
from data.product_card import NAME, REVIEW
import allure
import pytest

class TestProductCard:
    @pytest.mark.smoke
    @allure.title('Проверить отправку ревью товара')
    def test_fill_review(self, open_product_card, driver):
        product = ProductCard(driver)
        product.scroll_to_cart()
        product.click_reviews_tab()
        product.fill_review_name(NAME)
        product.fill_review(REVIEW)
        product.click_five_star_rating()
        product.click_continue_button()
