"""
Параметризуйте фикстуру несколькими вариантами размеров окна
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
"""
import random

import pytest
from selene.support.shared import browser
from selenium import webdriver


@pytest.fixture(params=[(1250, 700), (1500, 1050), (504, 340), (455, 550)])
def browser_open(request):
    chrome_options = webdriver.ChromeOptions()
    browser.config.driver_options = chrome_options
    browser.config.window_width = request.param[0]
    browser.config.window_height = request.param[1]
    yield browser
    browser.quit()


def test_github_desktop(browser_open):
    if browser._config.window_width < 1020:
        pytest.skip(reason='Пропускаем десктопный тест - соотношение сторон мобильное')
    browser.open('https://github.com')
    browser.element('[href="/login"]').click()


def test_github_mobile(browser_open):
    if browser._config.window_width > 1200:
        pytest.skip(reason='Пропускаем мобильный тест - соотношение сторон десктопное')
    browser.open('https://github.com')
    browser.element('[class="Button-content"]').click()
    browser.element('[href="/login"]').click()
