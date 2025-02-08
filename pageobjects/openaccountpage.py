from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from pageobjects.activitypage import ActivityPage

class OpenAccountPage():
    driver: Chrome

    # Declaring the page objects (fields & buttons)
    # There are two types of accounts: CHECKING and SAVINGS
    account_type: tuple = (By.ID, "type")
    source_account: tuple = (By.ID, "fromAccountId")
    open_account_button: tuple = (By.CSS_SELECTOR, "input[value='Open New Account']")
    account_opened: tuple = (By.ID, "openAccountResult")
    new_account_id: tuple = (By.ID, "newAccountId")

    # Declaring the error labels
    internal_error: tuple = (By.ID, "openAccountError")

    def __init__(self, driver):
        self._driver = driver

    def get_account_type(self) -> WebElement:
        """
        Returns the account type dropdown list.
        :return: webelement
        """
        return self._driver.find_element(*OpenAccountPage.account_type)

    def get_source_accounts(self) -> WebElement:
        """
        Returns the source account dropdown list.
        :return: webelement
        """
        return self._driver.find_element(*OpenAccountPage.source_account)

    def get_source_account(self):
        """
        Returns the source account number from the list.
        :return: int account number
        """
        pass

    def get_open_account_button(self) -> WebElement:
        """
        Returns the open new account button.
        :return: webelement
        """
        return self._driver.find_element(*OpenAccountPage.open_account_button)

    def get_account_opened_msg(self) -> WebElement:
        """
        Returns the account opened message.
        :return: webelement
        """
        return self._driver.find_element(*OpenAccountPage.account_opened)

    def get_new_account_id(self) -> ActivityPage:
        """
        Returns the new account id with a link.
        :return: page object
        """
        self._driver.find_element(*OpenAccountPage.new_account_id).click()
        return ActivityPage(self._driver)

    def get_internal_error(self)  -> WebElement:
        """
        Returns the internal error message.
        :return: webelement
        """
        return self._driver.find_element(*OpenAccountPage.internal_error)




