"""
Переопределите параметр с помощью indirect параметризации на уровне теста
"""
import pytest
from selene.support.shared import browser


@pytest.fixture(params=[(1200, 700), (375, 700), (900, 700), (500, 700)])
def browser_open(request):
    browser.open('https://github.com')
    browser.config.window_width = request.param[0]
    browser.config.window_height = request.param[1]
    yield browser
    browser.quit()


@pytest.mark.parametrize('browser_open', [(1200, 700), (900, 700)], indirect=True)
def test_github_desktop(browser_open):
    browser.element('[href="/login"]').click()


@pytest.mark.parametrize('browser_open', [(375, 700), (500, 700)], indirect=True)
def test_github_mobile(browser_open):
    browser.element('[class="Button-content"]').click()
    browser.element('[href="/login"]').click()
