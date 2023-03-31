from selene.support.shared import browser


def window_size(width, height):
    browser.driver.set_window_size(width, height)
