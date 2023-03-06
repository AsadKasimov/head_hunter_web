import allure
from selene.support.conditions import have
from selene.support.shared import browser
from hh_ru.model.controls.radiobut import radiobutton_click
from hh_ru.utils.scroll import scroll_to_


def open_search():
    with allure.step('Открывает страницу поиска'):
        browser.open('/search/vacancy/advanced')

def set_search_keyword(text):
    with allure.step(f'Вводит профессию {text}'):
        browser.element('[data-qa=vacancysearch__keywords-input]').send_keys(text)

def search_keyword_filter(text):
    with allure.step(f'Нажимает на искать только {text}'):
        radiobutton_click('[class="bloko-checkbox__text"]', text)

def scroll_to_profroles_switcher():
    with allure.step('Скроллит'):
        scroll_to_('[data-qa="resumesearch__profroles-switcher"]')

def set_prof(text):
    with allure.step(f'Точное обозначение профессии {text}'):
        browser.element('[data-qa="resumesearch__profroles-switcher"]').click()
        browser.element('[data-qa=bloko-tree-selector-popup-search]').type(text)
        browser.element('[data-qa~=bloko-tree-selector-item-text-124]').click()
        browser.element('[data-qa=bloko-tree-selector-popup-submit]').click()

def set_search_zone(text):
    with allure.step(f'Выбирает зону поиска как {text}'):
        browser.element('[data-qa=advanced-search-region-selectFromList]').click()
        browser.element('[data-qa=bloko-tree-selector-popup-search]').type(text)
        radiobutton_click('[data-qa~="bloko-tree-selector-item-text"]', text)
        browser.element('[data-qa=bloko-tree-selector-popup-submit]').click()

def scroll_to_work_experience():
    with allure.step('Скроллит'):
        scroll_to_('[data-qa=advanced-search__experience-item_between1And3]')

def click_work_experience(text):
    with allure.step(f'Выбирает опыт работы {text}'):
        radiobutton_click('[class="bloko-radio"]', text)

def set_type_of_employment(text):
    with allure.step(f'Выбирает тип занятости как {text}'):
        radiobutton_click('[class="bloko-form-item-baseline"]', text)

def set_work_schedule(text):
    with allure.step(f'Выбирает график работы как {text}'):
        radiobutton_click('[class="bloko-form-item-baseline"]', text)

def but_submit():
    with allure.step('Нажимает на кнопку "Найти"'):
        browser.element('[data-qa=advanced-search-submit-button]').click()

def assert_search(number):
    with allure.step(f'Проверка найденных вакансий больше {0}'):
        browser.all('[class="vacancy-serp-item__layout"]').should(have.size_greater_than(number))
