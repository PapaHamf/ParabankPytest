from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from pageobjects.basepage import BasePage

class AboutUs(BasePage):
    """
    Class that holds the locators of the About us page and methods to get its webelements.
    """
    driver: Chrome

    # Declaring the page objects
    PAGE_HEADER: tuple = (By.CLASS_NAME, "title")

    def __init__(self, driver):
        self._driver = driver

    def get_page_header(self) -> WebElement:
        """
        Returns the page header text.
        :return: webelement
        """
        return self.verify_element_presence(AboutUs.PAGE_HEADER)
