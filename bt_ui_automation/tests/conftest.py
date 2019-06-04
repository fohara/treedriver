import pytest
from selenium import webdriver

from bt_ui_automation.tests.page_objects.pages import Pages

IMPLICIT_WAIT = 1

@pytest.fixture
def pages(request):

    driver = webdriver.Firefox()
    driver.implicitly_wait(IMPLICIT_WAIT)
    _pages = Pages(driver)

    def teardown():
        if driver:
            driver.quit()

    request.addfinalizer(teardown)

    return _pages