import os

import allure
import pytest
from playwright import sync_playwright


@pytest.fixture(scope='session')
def page():
    with sync_playwright() as play:
        if os.getenv('DOCKER_RUN') or os.getenv('GITHUB_RUN'):
            browser = play.chromium.launch(headless=True, args=['--no-sandbox'])
        else:
            browser = play.chromium.launch(headless=False)
        page = browser.newPage()
        global PAGE
        PAGE = page
        yield page
        browser.close()


PAGE = None


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport():
    outcome = yield
    test_result = outcome.get_result()

    if test_result.when in ["setup", "call"]:
        xfail = hasattr(test_result, 'wasxfail')
        if test_result.failed or (test_result.skipped and xfail):
            global PAGE
            if PAGE:
                allure.attach(PAGE.screenshot(), name='screenshot', attachment_type=allure.attachment_type.PNG)
                allure.attach(PAGE.content(), name='html_source', attachment_type=allure.attachment_type.HTML)
