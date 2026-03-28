import pytest
from selene import browser


@pytest.fixture(scope="function", autouse=True)
def browser_setup():
    browser.config.driver_name = "chrome"
    browser.config.base_url = "https://todomvc.com/"
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config.timeout = 1

    yield
    browser.quit()