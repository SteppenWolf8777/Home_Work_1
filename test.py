from selene import browser
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-gpu')

browser.config.driver_options = options

def test_demo_aqa():
    browser.open('https://todomvc.com/')
    browser.quit()