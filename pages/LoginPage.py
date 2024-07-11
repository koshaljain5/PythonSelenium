from selenium.webdriver.common.by import By
from pages.BasePage import BasePage

class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    login_button_container = "login_button_container"
    login_username_field = "user-name"
    login_password_field = "password"
    login_button = "login-button"

    def input_text_in_field_on_login_page(self, element_name, input_text):
        base_page = BasePage(self.driver)
        base_page.find_element_by_property(element_name).send_keys(input_text)

    def click_btn_on_login_page(self, element_name):
        base_page = BasePage(self.driver)
        base_page.find_element_by_property(element_name).click()

    def element_is_visible_on_login_page(self, element_name):
        base_page = BasePage(self.driver)
        return base_page.find_element_by_property(element_name).is_displayed()

    def login_app(self):
        self.input_text_in_field_on_login_page(self.login_username_field, "standard_user")
        self.input_text_in_field_on_login_page(self.login_password_field, "secret_sauce")
        self.click_btn_on_login_page(self.login_button)