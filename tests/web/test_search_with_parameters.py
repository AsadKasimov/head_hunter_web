import allure
from hh_ru.model.pages import search_with_parameters


@allure.parent_suite('Web')
@allure.suite('Поиск')
@allure.title(f"Поиск профессии с параметрами")
def test_hh_serch():
    search_with_parameters.open_search()
    search_with_parameters.set_search_keyword('Тестировщик')
    search_with_parameters.search_keyword_filter("в названии вакансии")
    search_with_parameters.scroll_to_profroles_switcher()
    search_with_parameters.set_prof('Тестировщик')
    search_with_parameters.set_search_zone('Московская область')
    search_with_parameters.scroll_to_work_experience()
    search_with_parameters.click_work_experience("От 1 года до 3 лет")
    search_with_parameters.set_type_of_employment('Полная занятость')
    search_with_parameters.set_work_schedule('Полный день')
    search_with_parameters.but_submit()
    search_with_parameters.assert_search(0)
