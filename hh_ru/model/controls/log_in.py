import os
import time
import allure
from dotenv import load_dotenv
from selene.support.shared import browser

load_dotenv()
email = os.getenv('EMAIL')
password = os.getenv('PASSWORD')

def login_in_hh():
    with allure.step('Фикстура входа в аккаунт'):
        load_dotenv()
        browser.open('/account/login')
        browser.element('[data-qa="account-signup-email"]').type(email)
        time.sleep(2)
        browser.element('[data-qa="expand-login-by-password"]').click()
        time.sleep(2)
        browser.element('[data-qa="login-input-password"]').type(password)
        time.sleep(2)
        browser.element('[data-qa="account-login-submit"]').click()
        time.sleep(2)
