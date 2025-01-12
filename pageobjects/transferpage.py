from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

class TransferPage():
    driver: Chrome

    # Declaring the page objects (fields & buttons)
    amount: tuple = (By.ID, "amount")
    source_account: tuple = (By.ID, "fromAccountId")
    target_account: tuple = (By.ID, "toAccountId")
    transfer_button: tuple = (By.CSS_SELECTOR, "input[value='Transfer']")
    transfer_complete: tuple = (By.XPATH, "//h1[text()='Transfer Complete!']")
    amount_result: tuple = (By.ID, "amountResult")
    source_account_result: tuple = (By.ID, "fromAccountIdResult")
    target_account_result: tuple = (By.ID, "toAccountIdResult")

    # Declaring the error labels
    amount_error: tuple = (By.ID, "amount.errors")

    def __init__(self, driver):
        self._driver = driver

    def get_amount(self):
        """
        Returns the amount to transfer.
        :return: webelement
        """
        return self._driver.find_element(*TransferPage.amount)

    def get_source_account(self):
        """
        Returns the source account dropdown list.
        :return: webelement
        """
        return self._driver.find_element(*TransferPage.source_account)

    def get_target_account(self):
        """
        Returns the target account dropdown list.
        :return: webelement
        """
        return self._driver.find_element(*TransferPage.target_account)

    def get_transfer_button(self):
        """
        Returns the transfer button.
        :return: webelement
        """
        return self._driver.find_element(*TransferPage.transfer_button)

    def get_transfer_complete(self):
        """
        Returns the transfer complete message.
        :return: webelement
        """
        return self._driver.find_element(*TransferPage.transfer_complete)

    def get_amount_result(self):
        """
        Returns the amount of the completed transfer.
        :return: webelement
        """
        return self._driver.find_element(*TransferPage.amount_result)

    def get_source_account_result(self):
        """
        Returns the source account of the completed transfer.
        :return: webelement
        """
        return self._driver.find_element(*TransferPage.source_account_result)

    def get_target_account_result(self):
        """
        Returns the target account of the completed transfer.
        :return: webelement
        """
        return self._driver.find_element(*TransferPage.target_account_result)