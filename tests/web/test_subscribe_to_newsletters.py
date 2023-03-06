import allure
from hh_ru.model.controls.log_in import login_in_hh
from hh_ru.model.pages import subscribe_to_newsletters


@allure.parent_suite('Web')
@allure.suite('Рассылка')
@allure.title(f"Подписка на рассылку на почту")
def test_set_favorites():
    login_in_hh()

    subscribe_to_newsletters.set_favorites_profession('Тестировщик')
    subscribe_to_newsletters.click_subscribe()
    subscribe_to_newsletters.assert_subscribe()
