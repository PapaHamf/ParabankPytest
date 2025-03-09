from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from pageobjects.basepage import BasePage

class IntInboxPage(BasePage):
    driver: Chrome

    # Declaring external locators (email provider)
    EMAIL_SENDER_INT: tuple = (By.CLASS_NAME, "msglist-item__message__sender")

    def __init__(self, driver):
        self._driver = driver

    def get_external_message_senders(self) -> list[WebElement]:
        """
        Returns the list of webelements with the sender names.
        :return:
        """
        return self.verify_elements_presence(IntInboxPage.EMAIL_SENDER_INT)