from selene.support.conditions import be
from selene.support.shared import browser
import allure

def type_professional(text):
    with allure.step(f'Ввод в поисковое поле: {text}'):
        browser.element('[data-qa="search-input"]').type(text).press_enter()

def click_favorite():
    with allure.step(f'Добавление вакансии в Избранные, нажатием на кнопку'):
        browser.all('[data-qa="vacancy-search-mark-favorite_false"]')[0].click()

def assert_favorite():
    with allure.step(f'Проверка добавления в избранные'):
        assert browser.all('[data-qa="vacancy-search-mark-favorite_true"]')[0].wait_until(be.visible)

def set_in_blacklist():
    with allure.step(f'Добавление вакансии в Черный список'):
        browser.all('[data-qa="vacancy__blacklist-show-add"]')[0].click()
        browser.element('[data-qa="vacancy__blacklist-menu-add-vacancy"]').click()
