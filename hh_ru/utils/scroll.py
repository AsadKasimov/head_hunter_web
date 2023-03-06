from selene.core import command
from selene.support.shared import browser

def scroll_to_(selector):
    browser.element(selector).perform(command.js.scroll_into_view)
