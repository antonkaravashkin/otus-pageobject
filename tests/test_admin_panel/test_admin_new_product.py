from src.admin_panel.admin_panel import AdminPanel
from data.admin_panel import (
    PRODUCT_NAME,
    MODEL,
    META_TAG,
    NO_RESULTS,
)


class TestProducts:
    def test_create_new_product(self, admin_panel_login, driver):
        admin = AdminPanel(driver)
        admin.click_catalog()
        admin.click_product()
        admin.click_new_product()
        admin.click_general_tab()
        admin.input_product_name(PRODUCT_NAME)
        admin.input_meta_tag(META_TAG)
        admin.click_data_tab()
        admin.input_model(MODEL)
        admin.click_save_button()
        admin.assert_created_product_exist()

    def test_delete_products(self, admin_panel_login, driver):
        admin = AdminPanel(driver)
        admin.click_catalog()
        admin.click_product()
        admin.check_product_for_delete()
        admin.click_delete_button()
        admin.accept_alert()
        admin.input_filter_model(MODEL)
        admin.click_filter_button()
        admin.assert_no_filter_result(NO_RESULTS)
