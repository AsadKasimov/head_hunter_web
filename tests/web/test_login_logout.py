import allure
from hh_ru.model.pages import login_logout


@allure.parent_suite('Web')
@allure.suite('Авторизация')
@allure.title(f"Вход и Выход из аккаунта")
def test_log_in_log_out():
    login_logout.open_login_page()
    login_logout.set_login()
    login_logout.selecting_password()
    login_logout.set_password()
    login_logout.enter_submit()
    login_logout.click_profile_menu()
    login_logout.logoffuser()
    login_logout.assert_logoff()
