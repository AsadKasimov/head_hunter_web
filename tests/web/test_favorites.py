import allure
from hh_ru.model.controls.log_in import login_in_hh
from hh_ru.model.pages import favorites


@allure.parent_suite('Web')
@allure.suite('Избранные и Черный список для вакансий')
@allure.title(f"Добавление вакансий в Избранные и Черный список")
def test_set_favorites():
    login_in_hh()

    favorites.type_professional('Тестировщик')
    favorites.click_favorite()
    favorites.assert_favorite()
    favorites.set_in_blacklist()
