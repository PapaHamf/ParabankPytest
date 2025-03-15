from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from pageobjects.activitypage import ActivityPage
from pageobjects.basepage import BasePage

class OpenAccountPage(BasePage):
    """
    Class that holds the locators of the Open account page and methods to get its webelements.
    """
    driver: Chrome

    # Declaring the page objects (fields & buttons)
    # There are two types of accounts: CHECKING and SAVINGS
    ACCOUNT_TYPE: tuple = (By.ID, "type")
    SOURCE_ACCOUNT: tuple = (By.ID, "fromAccountId")
    OPEN_ACCOUNT_BUTTON: tuple = (By.CSS_SELECTOR, "input[value='Open New Account']")
    ACCOUNT_OPENED: tuple = (By.ID, "openAccountResult")
    SUCCESS_TITLE: tuple = (By.CLASS_NAME, "title")
    NEW_ACCOUNT_ID: tuple = (By.ID, "newAccountId")

    # Declaring the error labels
    INTERNAL_ERROR: tuple = (By.ID, "openAccountError")
    ERROR_TITLE: tuple = (By.CLASS_NAME, "title")

    # Declaring the success and errors messages
    OPEN_SUCCESS_MSG = "Account Opened!"
    OPEN_ERROR_MSG = "Error!"

    def __init__(self, driver):
        self._driver = driver

    def get_account_type(self) -> WebElement:
        """
        Returns the account type dropdown list.
        :return: webelement
        """
        return self.verify_element_presence(OpenAccountPage.ACCOUNT_TYPE)

    def get_source_accounts(self) -> WebElement:
        """
        Returns the source account dropdown list.
        :return: webelement
        """
        return self.verify_element_presence(OpenAccountPage.SOURCE_ACCOUNT)

    def get_source_accounts_text(self) -> list[str]:
        """
        Returns the source accounts numbers as strings.
        :return: List of account numbers strings
        """
        return self.get_list_values(self.get_source_accounts())

    def get_open_account_button(self) -> WebElement:
        """
        Returns the open new account button.
        :return: webelement
        """
        return self.verify_element_presence(OpenAccountPage.OPEN_ACCOUNT_BUTTON)

    def get_account_opened_msg(self) -> WebElement:
        """
        Returns the account opened message.
        :return: webelement
        """
        return self.verify_element_presence(OpenAccountPage.ACCOUNT_OPENED)

    def get_success_title(self) -> WebElement:
        """
        Returns the account opened success message title.
        :return: webelement
        """
        return self.get_account_opened_msg().find_element(*OpenAccountPage.SUCCESS_TITLE)

    def get_new_account_id(self) -> ActivityPage:
        """
        Returns the new account activity page object.
        :return: page object
        """
        self.verify_element_presence(OpenAccountPage.NEW_ACCOUNT_ID).click()
        return ActivityPage(self._driver)

    def get_internal_error(self)  -> WebElement:
        """
        Returns the internal error message.
        :return: webelement
        """
        return self.verify_element_presence(OpenAccountPage.INTERNAL_ERROR)

    def get_error_title(self) -> WebElement:
        """
        Returns the account opened error message title.
        :return: webelement
        """
        return self.get_internal_error().find_element(*OpenAccountPage.ERROR_TITLE)




