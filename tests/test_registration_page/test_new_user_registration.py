import allure
from src.user_registration.registration_page import (
    RegistrationPage,
)
from data.user_registration import (
    SUCCESS_ACCOUNT_CREATION,
    FIRST_NAME,
    LAST_NAME,
    E_MAIL,
    TELEPHONE,
    PASSWORD,
)


class TestCreateNewUser:
    @allure.title('Проверяем создание пользователя')
    def test_create_new_user(self, my_account_registration, driver):
        user = RegistrationPage(driver)
        user.input_first_name(FIRST_NAME)
        user.input_last_name(LAST_NAME)
        user.input_email(E_MAIL)
        user.input_telephone(TELEPHONE)
        user.input_password(PASSWORD)
        user.input_password_confirmation(PASSWORD)
        user.click_privacy_checkbox()
        user.submit_form()
        user.assert_account_creation_text(SUCCESS_ACCOUNT_CREATION)
