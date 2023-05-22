"""
Параметризуйте фикстуру несколькими вариантами размеров окна
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
"""
import random

import pytest
from selene.support.shared import browser


@pytest.fixture()
def browser_open():
    browser.open('https://github.com')
    browser.config.window_width = random.randint(375, 1500)

def test_github_desktop(browser_open):
    if browser.config.window_width <= 1012:
        pytest.skip('Пропускаем десктопный тест, если соотношение сторон мобильное')
    else:
        browser.element('[href="/login"]').click()

def test_github_mobile(browser_open):
    if browser.config.window_width >= 1011:
        pytest.skip('Пропускаем мобильный тест, если соотношение сторон десктопное')
    else:
        browser.element('[class="Button-content"]').click()
        browser.element('[href="/login"]').click()
