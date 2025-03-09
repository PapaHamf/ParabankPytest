from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from pageobjects.basepage import BasePage
from pageobjects.intinboxpage import IntInboxPage

class IntMailPage(BasePage):
    driver: Chrome

    TICKET_SERVER = "poczta.int.pl"
    TICKET_EMAIL = "mareczek_testowy@int.pl"
    TICKET_PASSWORD = "m4reczek1234!"

    # Declaring external locators (email provider)
    EMAIL_ADDRESS_INT: tuple = (By.ID, "emailId")
    EMAIL_PASSWORD_INT: tuple = (By.ID, "passwordId")
    EMAIL_LOGIN_BUTTON_INT: tuple = (By.CSS_SELECTOR, "button[type='submit']")

    def __init__(self, driver):
        self._driver = driver

    def get_external_email_address(self) -> WebElement:
        """
        Returns the external email address field.
        :return:
        """
        return self.verify_element_presence(IntMailPage.EMAIL_ADDRESS_INT)

    def get_external_password(self) -> WebElement:
        """
        Returns the external password field.
        :return:
        """
        return self.verify_element_presence(IntMailPage.EMAIL_PASSWORD_INT)

    def get_external_login_button(self) -> IntInboxPage:
        """
        Returns the external login button.
        :return:
        """
        self.verify_element_presence(IntMailPage.EMAIL_LOGIN_BUTTON_INT).click()
        return IntInboxPage(self._driver)