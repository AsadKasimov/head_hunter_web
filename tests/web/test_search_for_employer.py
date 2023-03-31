import allure
import pytest
from hh_ru.model.pages import search_for_employer
from hh_ru.utils.set_window_size import window_size


@allure.parent_suite('Web')
@allure.suite('Работодатель')
@allure.title(f"Поиск резюме без парамтров")
@pytest.mark.parametrize('width, height', [(1080, 720), (900, 300)])
def test_search_resume(width, height):
    window_size(width, height)
    search_for_employer.open_for_employer()
    search_for_employer.scroll_to_search_zone()
    search_for_employer.set_searh_resume('Тестировщик')
    search_for_employer.assert_search_size_greater(0)
