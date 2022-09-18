from src.user_registration.registration_page import RegistrationPage
import allure


class TestRegistrationPage:
    @allure.title('Проверяем наличие элементов страницы регистрации')
    def test_check_elements(self, my_account_registration, driver):
        registration = RegistrationPage(driver)
        registration.assert_personal_details()
        registration.assert_telephone_field()
        registration.assert_password_title()
        registration.assert_newsletter()
        registration.assert_subscribe_block()
