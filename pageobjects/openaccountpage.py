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
    NEW_ACCOUNT_ID: tuple = (By.ID, "newAccountId")

    # Declaring the error labels
    INTERNAL_ERROR: tuple = (By.ID, "openAccountError")

    def __init__(self, driver):
        self._driver = driver

    def get_account_type(self) -> WebElement:
        """
        Returns the account type dropdown list.
        :return: webelement
        """
        return self._driver.find_element(*OpenAccountPage.ACCOUNT_TYPE)

    def get_source_accounts(self) -> WebElement:
        """
        Returns the source account dropdown list.
        :return: webelement
        """
        return self._driver.find_element(*OpenAccountPage.SOURCE_ACCOUNT)

    def get_open_account_button(self) -> WebElement:
        """
        Returns the open new account button.
        :return: webelement
        """
        return self._driver.find_element(*OpenAccountPage.OPEN_ACCOUNT_BUTTON)

    def get_account_opened_msg(self) -> WebElement:
        """
        Returns the account opened message.
        :return: webelement
        """
        return self._driver.find_element(*OpenAccountPage.ACCOUNT_OPENED)

    def get_new_account_id(self) -> ActivityPage:
        """
        Returns the new account id with a link.
        :return: page object
        """
        self._driver.find_element(*OpenAccountPage.NEW_ACCOUNT_ID).click()
        return ActivityPage(self._driver)

    def get_internal_error(self)  -> WebElement:
        """
        Returns the internal error message.
        :return: webelement
        """
        return self._driver.find_element(*OpenAccountPage.INTERNAL_ERROR)




