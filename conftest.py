from selenium import webdriver
import pytest
import allure

@pytest.fixture()
def browser():
    #browser = webdriver.Firefox()
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    # открываем браузер
    local = "https://stilsoft.ru/products/kitsoz-synerget"
    browser.get(local)

    # закрываем браузер
    yield browser
    browser.quit()
