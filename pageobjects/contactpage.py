from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

class ContactPage():
    """
    Class that holds the locators of the Contact page and methods to get its webelements.
    """
    driver: Chrome

    MESSAGE_BODY_WIDTH: float = 300
    MESSAGE_BODY_HEIGHT: float = 126

    # Declaring the page objects (fields & buttons)
    NAME: tuple = (By.ID, "name")
    EMAIL_ADDRESS: tuple = (By.ID, "email")
    PHONE_NUMBER: tuple = (By.ID, "phone")
    MESSAGE_BODY: tuple = (By.ID, "message")
    SEND_BUTTON: tuple = (By.CSS_SELECTOR, "input[value='Send to Customer Care']")

    # Declaring the error labels
    NAME_ERROR: tuple = (By.ID, "name.errors")
    EMAIL_ERROR: tuple = (By.ID, "email.errors")
    PHONE_NUMBER_ERROR: tuple = (By.ID, "phone.errors")
    MESSAGE_BODY_ERROR: tuple = (By.ID, "message.errors")

    # Success message
    SUCCESS_MSG: tuple = (By.XPATH, "//div[@id='rightPanel']/p[1]")

    def __init__(self, driver):
        self._driver = driver

    def get_name(self) -> WebElement:
        """
        Returns the name field.
        :return: webelement
        """
        return self._driver.find_element(*ContactPage.NAME)

    def get_email_address(self) -> WebElement:
        """
        Returns the e-mail address field.
        :return: webelement
        """
        return self._driver.find_element(*ContactPage.EMAIL_ADDRESS)

    def get_phone_number(self) -> WebElement:
        """
        Returns the phone number field.
        :return: webelement
        """
        return self._driver.find_element(*ContactPage.PHONE_NUMBER)

    def get_message_body(self) -> WebElement:
        """
        Returns the message body field.
        :return: webelement
        """
        return self._driver.find_element(*ContactPage.MESSAGE_BODY)

    def get_send_button(self) -> WebElement:
        """
        Returns the send message button.
        :return: webelement
        """
        return self._driver.find_element(*ContactPage.SEND_BUTTON)

    def get_name_error(self) -> WebElement:
        """
        Returns the name field error text.
        :return: webelement
        """
        return self._driver.find_element(*ContactPage.NAME_ERROR)

    def get_email_address_error(self) -> WebElement:
        """
        Returns the email address field error text.
        :return: webelement
        """
        return self._driver.find_element(*ContactPage.EMAIL_ERROR)

    def get_phone_number_error(self) -> WebElement:
        """
        Returns the phone number field error text.
        :return: webelement
        """
        return self._driver.find_element(*ContactPage.PHONE_NUMBER_ERROR)

    def get_message_body_error(self) -> WebElement:
        """
        Returns the message body field error text.
        :return: webelement
        """
        return self._driver.find_element(*ContactPage.MESSAGE_BODY_ERROR)

    def get_success_message(self) -> WebElement:
        """
        Returns the successful sending text.
        :return: webelement
        """
        return self._driver.find_element(*ContactPage.SUCCESS_MSG)