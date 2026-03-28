from pathlib import Path
from selene import browser, have

browser.config.driver_name = "chrome"
browser.config.base_url = "https://todomvc.com/"
browser.config.window_width = 1920
browser.config.window_height = 1080
browser.config.timeout = 1


def test_demo_aqa():
    browser.open('https://todomvc.com/')

    browser.quit()