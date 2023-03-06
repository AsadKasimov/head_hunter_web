from hh_ru.model.pages import search_for_employer

def test_search_resume():
    search_for_employer.open_for_employer()
    search_for_employer.scroll_to_search_zone()
    search_for_employer.set_searh_resume('Тестировщик')
    search_for_employer.assert_search_size_greater(0)
