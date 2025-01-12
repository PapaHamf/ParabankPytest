from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

class OpenAccountPage():
    driver: Chrome

    # Declaring the page objects (fields & buttons)
    account_type: tuple = (By.ID, "type")
    source_account: tuple = (By.ID, "fromAccountId")
    open_account_button: tuple = (By.CSS_SELECTOR, "input[value='Open New Account']")
    account_opened: tuple = (By.CSS_SELECTOR, "div#openAccountResult h1.title")
    new_account_id: tuple = (By.ID, "newAccountId")

    def __init__(self, driver):
        self._driver = driver

    def get_account_type(self):
        """
        Returns the account type dropdown list.
        :return: webelement
        """
        return self._driver.find_element(*OpenAccountPage.account_type)

    def get_source_account(self):
        """
        Returns the source account dropdown list.
        :return: webelement
        """
        return self._driver.find_element(*OpenAccountPage.source_account)

    def get_open_account_button(self):
        """
        Returns the open new account button.
        :return: webelement
        """
        return self._driver.find_element(*OpenAccountPage.open_account_button)

    def get_account_opened_msg(self):
        """
        Returns the account opened message.
        :return: webelement
        """
        return self._driver.find_element(*OpenAccountPage.account_opened)

    def get_new_account_id(self):
        """
        Returns the new account id with a link.
        :return: webelement
        """
        return self._driver.find_element(*OpenAccountPage.new_account_id)



