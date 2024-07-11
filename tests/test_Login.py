import pytest

from pages.HomePage import HomePage
from pages.LoginPage import LoginPage


@pytest.mark.usefixtures("setup_and_teardown")
class TestLogin:
    def test_login_a_user(self):
        login_page = LoginPage(self.driver)
        home_page = HomePage(self.driver)
        login_page.login_app()
        assert home_page.element_is_visible_on_home_page(home_page.home_inventory_container)
        home_page.logout_app()

    def test_logout(self):
        login_page = LoginPage(self.driver)
        home_page = HomePage(self.driver)
        login_page.login_app()
        home_page.click_btn_on_home_page(home_page.home_hamburger_left_btn)
        home_page.click_btn_on_home_page(home_page.home_logout_btn)
        assert login_page.element_is_visible_on_login_page(login_page.login_button_container)
