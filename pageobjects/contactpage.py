from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

class ContactPage():
    driver: Chrome

    # Declaring the page objects (fields & buttons)
    name: tuple = (By.ID, "name")
    email_address: tuple = (By.ID, "email")
    phone_number: tuple = (By.ID, "phone")
    message_body: tuple = (By.ID, "message")
    send_button: tuple = (By.CSS_SELECTOR, "input[value='Send to Customer Care']")

    # Declaring the error labels
    name_error: tuple = (By.ID, "name.errors")
    email_error: tuple = (By.ID, "email.errors")
    phone_number_error: tuple = (By.ID, "phone.errors")
    message_body_error: tuple = (By.ID, "message.errors")

    # Success message
    success_msg: tuple = (By.XPATH, "//div[@id='rightPanel']/p[1]")

    def __init__(self, driver):
        self._driver = driver

    def get_name(self) -> WebElement:
        """
        Returns the name field.
        :return: webelement
        """
        return self._driver.find_element(*ContactPage.name)

    def get_email_address(self) -> WebElement:
        """
        Returns the e-mail address field.
        :return: webelement
        """
        return self._driver.find_element(*ContactPage.email_address)

    def get_phone_number(self) -> WebElement:
        """
        Returns the phone number field.
        :return: webelement
        """
        return self._driver.find_element(*ContactPage.phone_number)

    def get_message_body(self) -> WebElement:
        """
        Returns the message body field.
        :return: webelement
        """
        return self._driver.find_element(*ContactPage.message_body)

    def get_send_button(self) -> WebElement:
        """
        Returns the send message button.
        :return: webelement
        """
        return self._driver.find_element(*ContactPage.send_button)

    def get_name_error(self) -> WebElement:
        """
        Returns the name field error text.
        :return: webelement
        """
        return self._driver.find_element(*ContactPage.name_error)

    def get_email_address_error(self) -> WebElement:
        """
        Returns the email address field error text.
        :return: webelement
        """
        return self._driver.find_element(*ContactPage.email_error)

    def get_phone_number_error(self) -> WebElement:
        """
        Returns the phone number field error text.
        :return: webelement
        """
        return self._driver.find_element(*ContactPage.phone_number_error)

    def get_message_body_error(self) -> WebElement:
        """
        Returns the message body field error text.
        :return: webelement
        """
        return self._driver.find_element(*ContactPage.message_body_error)

    def get_success_message(self) -> WebElement:
        """
        Returns the successful sending text.
        :return: webelement
        """
        return self._driver.find_element(*ContactPage.success_msg)