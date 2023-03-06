from selene.support.conditions import have
from selene.support.shared import browser

def radiobutton_click(seletor, value):
    browser.all(seletor).element_by(have.text(value)).click()
