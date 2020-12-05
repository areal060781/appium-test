import pytest
from appium import webdriver

from helpers.appiumsetup import EXECUTOR, ANDROID_BASE_CAPS
from helpers.testdata import username, password, bad_password
from screens.login import Login as LoginScreen
from screens.main import Main as MainScreen


@pytest.fixture
def browser():
    driver = webdriver.Remote(EXECUTOR, ANDROID_BASE_CAPS)
    driver.implicitly_wait(10)

    yield driver

    driver.quit()


def test_login_message_correctness(browser):
    login_activity = LoginScreen(browser)
    login_activity.login(username, password)
    main_activity = MainScreen(browser)
    main_activity.validate_welcome_message(username)


def test_login_button_is_disabled_if_password_is_short(browser):
    login_activity = LoginScreen(browser)
    login_activity.login(username, bad_password)
    login_activity.validate_button_disabled_when_bad_password()
