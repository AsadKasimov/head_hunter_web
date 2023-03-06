import os
import time

import allure
from dotenv import load_dotenv
from selene.support.conditions import be
from selene.support.shared import browser

load_dotenv()
email = os.getenv('EMAIL')
password = os.getenv('PASSWORD')


def open_login_page():
    with allure.step(f'Открытие стриницы входа'):
        browser.open('/account/login')


def set_login():
    with allure.step(f'Ввод эл-почты: {email}'):
        browser.element('[data-qa="account-signup-email"]').type(email)
        time.sleep(2)


def selecting_password():
    with allure.step(f'Выбор входа через пароль'):
        browser.element('[data-qa="expand-login-by-password"]').click()


def set_password():
    with allure.step(f'Ввод пароля: {password}'):
        time.sleep(2)
        browser.element('[data-qa="login-input-password"]').type(password)


def enter_submit():
    with allure.step(f'Нажатие на кнопку "Вход"'):
        time.sleep(2)
        browser.element('[data-qa="account-login-submit"]').click()


def click_profile_menu():
    with allure.step(f'Нажатие на кнопку Профиля'):
        time.sleep(2)
    browser.element('[data-qa="mainmenu_applicantProfile"]').click()


def logoffuser():
    with allure.step(f'Кликнуть на "Выход"'):
        time.sleep(2)
        browser.element('[data-qa="mainmenu_logoffUser"]').click()


def assert_logoff():
    with allure.step(f'Проверка выхода'):
        assert browser.element('[data-qa="login"]').wait_until(be.visible)
