from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.config import BASE_URL


def test_success_login(driver):
    login = LoginPage(driver)
    inventory = InventoryPage(driver)

    login.open(BASE_URL)
    login.login("standard_user", "secret_sauce")

    assert inventory.is_opened()


def test_wrong_password(driver):
    login = LoginPage(driver)

    login.open(BASE_URL)
    login.login("standard_user", "wrong_password")

    assert "do not match" in login.get_error_text()


def test_locked_user(driver):
    login = LoginPage(driver)

    login.open(BASE_URL)
    login.login("locked_out_user", "secret_sauce")

    assert "locked out" in login.get_error_text()


def test_empty_fields(driver):
    login = LoginPage(driver)

    login.open(BASE_URL)
    login.login()

    assert "Username is required" in login.get_error_text()


def test_performance_user(driver):
    login = LoginPage(driver)
    inventory = InventoryPage(driver)

    login.open(BASE_URL)
    login.login("performance_glitch_user", "secret_sauce")

    assert inventory.is_opened()
