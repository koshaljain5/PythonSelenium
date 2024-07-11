import pytest
from pages.HomePage import HomePage
from pages.LoginPage import LoginPage


@pytest.mark.usefixtures("setup_and_teardown")
class TestSort:
    def test_sort_low_to_high(self):
        login_page = LoginPage(self.driver)
        home_page = HomePage(self.driver)
        login_page.login_app()
        home_page.select_element_by_text_home_page(home_page.home_sort_dropdown, "Price (low to high)")
        prices = home_page.get_text_of_all_elements(home_page.home_inventory_item_price)
        price_texts = [float(price.text.replace("$", "")) for price in prices]
        assert all(price_texts[i] <= price_texts[i + 1] for i in range(len(price_texts) - 1))
        home_page.logout_app()

    def test_sort_high_to_low(self):
        login_page = LoginPage(self.driver)
        home_page = HomePage(self.driver)
        login_page.login_app()
        home_page.select_element_by_text_home_page(home_page.home_sort_dropdown, "Price (high to low)")
        prices = home_page.get_text_of_all_elements(home_page.home_inventory_item_price)
        price_texts = [float(price.text.replace("$", "")) for price in prices]
        assert all(price_texts[i] >= price_texts[i + 1] for i in range(len(price_texts) - 1))
        home_page.logout_app()