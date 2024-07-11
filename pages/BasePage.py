from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element_by_property(self, property_value, multiple=False):
        locators = [By.ID, By.CLASS_NAME, By.NAME, By.XPATH, By.CSS_SELECTOR, By.LINK_TEXT, By.PARTIAL_LINK_TEXT]
        elements = []
        for locator in locators:
            try:
                if multiple:
                    found_elements = self.driver.find_elements(locator, property_value)
                    elements.extend(found_elements)
                else:
                    element = self.driver.find_element(locator, property_value)
                if element:
                    return element
            except Exception:
                pass

        if multiple:
            return elements
        else:
            raise NoSuchElementException(f"No element found with property: {property_value}")
