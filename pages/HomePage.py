from selenium.webdriver.support.select import Select
from pages.BasePage import BasePage

class HomePage:

    def __init__(self, driver):
        self.driver = driver

    home_hamburger_left_btn = "react-burger-menu-btn"
    home_logout_btn = "logout_sidebar_link"
    home_inventory_container = "inventory_container"
    home_sort_dropdown = "select[data-test='product-sort-container']"
    home_inventory_item_price = "div[class='inventory_item_price']"

    def click_btn_on_home_page(self, element_name):
        base_page = BasePage(self.driver)
        base_page.find_element_by_property(element_name).click()

    def element_is_visible_on_home_page(self, element_name):
        base_page = BasePage(self.driver)
        return base_page.find_element_by_property(element_name).is_displayed()

    def select_element_by_text_home_page(self, element_name, item_text):
        base_page = BasePage(self.driver)
        select = Select(base_page.find_element_by_property(element_name))
        select.select_by_visible_text(item_text)

    def get_text_of_all_elements(self, element_name):
        base_page = BasePage(self.driver)
        elements = base_page.find_element_by_property(element_name, multiple=True)
        element_texts = [element for element in elements]
        return element_texts

    def logout_app(self):
        self.click_btn_on_home_page(self.home_hamburger_left_btn)
        self.click_btn_on_home_page(self.home_logout_btn)
