from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webelement import WebElement

from pageobjects.basepage import BasePage

class ContactPage(BasePage):
    """
    Class that holds the locators of the Contact page and methods to get its webelements.
    """
    driver: Chrome

    MESSAGE_BODY_WIDTH: int = 300
    MESSAGE_BODY_HEIGHT: int = 126
    MESSAGE_SENTENCES: int = 5

    # Declaring the page objects (fields & buttons)
    NAME: tuple = (By.ID, "name")
    EMAIL_ADDRESS: tuple = (By.ID, "email")
    PHONE_NUMBER: tuple = (By.ID, "phone")
    MESSAGE_BODY: tuple = (By.ID, "message")
    SEND_BUTTON: tuple = (By.CSS_SELECTOR, "input[value='Send to Customer Care']")

    # Declaring the error labels
    ERROR_LABEL: tuple = (By.CLASS_NAME, "error")
    NAME_ERROR: tuple = (By.ID, "name.errors")
    EMAIL_ERROR: tuple = (By.ID, "email.errors")
    PHONE_NUMBER_ERROR: tuple = (By.ID, "phone.errors")
    MESSAGE_BODY_ERROR: tuple = (By.ID, "message.errors")

    # Success message
    SUCCESS_MSG: tuple = (By.XPATH, "//div[@id='rightPanel']/p[1]")

    # Declaring the success & errors messages
    ERROR_REQUIRED_MSG = " is required."
    ERROR_INVALID_MSG = " is invalid."
    CUSTOMER_CARE_SUCCESS_MSG = "Thank you "
    VALID_PAGE_TITLE = "ParaBank | Customer Care"
    # Full text "An internal error has occurred and has been logged."
    GENERAL_ERROR_MSG = "internal error"

    def __init__(self, driver):
        self._driver = driver

    def get_name(self) -> WebElement:
        """
        Returns the name field.
        :return: webelement
        """
        return self.verify_element_presence(ContactPage.NAME)

    def get_email_address(self) -> WebElement:
        """
        Returns the e-mail address field.
        :return: webelement
        """
        return self.verify_element_presence(ContactPage.EMAIL_ADDRESS)

    def get_phone_number(self) -> WebElement:
        """
        Returns the phone number field.
        :return: webelement
        """
        return self.verify_element_presence(ContactPage.PHONE_NUMBER)

    def get_message_body(self) -> WebElement:
        """
        Returns the message body field.
        :return: webelement
        """
        return self.verify_element_presence(ContactPage.MESSAGE_BODY)

    def resize_message_body_text_area(self) -> None:
        """
        Resizes the message body text area.
        :return:
        """
        textarea_size = self.get_message_body().size
        action = ActionChains(self._driver)
        action.move_to_element_with_offset(self.get_message_body(),
                                           int(( textarea_size["width"] - 6 ) / 2),
                                           int(( textarea_size["height"] - 6 ) / 2)) \
            .click_and_hold() \
            .move_by_offset(100, 100) \
            .release() \
            .perform()

    def get_message_body_size(self) -> tuple[int]:
        """
        Returns the tuple with the width and height of the text area.
        :return: Width and height of text area
        """
        sizes = self.get_message_body().get_attribute("style").split(";")
        width = int(sizes[0].split(":")[1].rstrip("px"))
        height = int(sizes[1].split(":")[1].rstrip("px"))
        return width, height

    def get_send_button(self) -> WebElement:
        """
        Returns the send message button.
        :return: webelement
        """
        return self.verify_element_clickable(ContactPage.SEND_BUTTON)

    def get_errors(self) -> int:
        """
        Returns the number of errors on the page.
        :return:
        """
        return len(self.verify_elements_presence(ContactPage.ERROR_LABEL))

    def get_name_error(self) -> WebElement:
        """
        Returns the name field error text.
        :return: webelement
        """
        return self.verify_element_presence(ContactPage.NAME_ERROR)

    def get_email_address_error(self) -> WebElement:
        """
        Returns the email address field error text.
        :return: webelement
        """
        return self.verify_element_presence(ContactPage.EMAIL_ERROR)

    def get_phone_number_error(self) -> WebElement:
        """
        Returns the phone number field error text.
        :return: webelement
        """
        return self.verify_element_presence(ContactPage.PHONE_NUMBER_ERROR)

    def get_message_body_error(self) -> WebElement:
        """
        Returns the message body field error text.
        :return: webelement
        """
        return self.verify_element_presence(ContactPage.MESSAGE_BODY_ERROR)

    def get_success_message(self) -> WebElement:
        """
        Returns the successful sending text.
        :return: webelement
        """
        return self.verify_element_presence(ContactPage.SUCCESS_MSG)

    def get_page_title(self) -> str:
        """
        Returns the page title.
        :return:
        """
        return self._driver.title