from selene.support.conditions import have
from selene.support.shared import browser
from hh_ru.utils.scroll import scroll_to_


def open_for_employer():
    browser.open('/employer')

def scroll_to_search_zone():
    scroll_to_('[data-qa="employer-index-search-input"]')

def set_searh_resume(text: str):
    browser.element('[data-qa="employer-index-search-input"]').type(text).press_enter()

def assert_search_size_greater(number):
    browser.all('[data-qa="resume-serp__resume"]').should(have.size_greater_than(number))
