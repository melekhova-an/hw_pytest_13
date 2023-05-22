"""
Сделайте разные фикстуры для каждого теста, которые выставят размеры окна браузера
"""
import pytest
from selene.support.shared import browser


@pytest.fixture(params=[(1200, 700), (900, 700)])
def browser_open_for_desktop(request):
    browser.open('https://github.com')
    browser.config.window_width = request.param[0]
    browser.config.window_height = request.param[1]
    yield browser
    browser.quit()


@pytest.fixture(params=[(375, 700), (500, 700)])
def browser_open_for_mobile(request):
    browser.open('https://github.com')
    browser.config.window_width = request.param[0]
    browser.config.window_height = request.param[1]
    yield browser
    browser.quit()


def test_github_desktop(browser_open_for_desktop):
    browser.element('[href="/login"]').click()


def test_github_mobile(browser_open_for_mobile):
    browser.element('[class="Button-content"]').click()
    browser.element('[href="/login"]').click()
