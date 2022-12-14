from src.admin_panel.admin_panel import AdminPanel
from data.admin_panel import FOOTER_TEXT
import allure
import pytest

@pytest.mark.admin_panel
@pytest.mark.xfail
class TestAdminPanelLanding:
    @allure.title('Проверяем страницу Админ Панели')
    def test_landing(self, driver):
        admin = AdminPanel(driver)
        admin.assert_panel_header_visible()
        admin.assert_username_label_visible()
        admin.assert_password_label_visible()
        admin.assert_footer_text(FOOTER_TEXT)
        admin.click_footer_opencart_link()
