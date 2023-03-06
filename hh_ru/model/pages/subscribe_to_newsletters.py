import allure
from selene.support.conditions import have
from selene.support.shared import browser

def set_favorites_profession(text):
    with allure.step(f'Ввод профессии в поисковую строку и нажатие на Enter'):
        browser.element('[data-qa="search-input"]').type(text).press_enter()
def click_subscribe():
    with allure.step(f'Нажатие на кнопку подписки'):
        browser.element('[data-qa="autosearch-subscribe__email-button"]').click()
def assert_subscribe():
    with allure.step(f'Проверка подписки'):
        browser.element('[data-qa="vacancy-serp__search-saved"]').should(have.text('Вы будете получать уведомления о новых вакансия на адрес: '))
