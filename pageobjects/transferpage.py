from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

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
    # Possible values:
    # 1. The amount cannot be empty.
	# 2. Please enter a valid amount.
    amount_errors: tuple = (By.ID, "amount.errors")
    # Probably not used
    internal_error: tuple = (By.ID, "showError")

    def __init__(self, driver):
        self._driver = driver

    def get_amount(self) -> WebElement:
        """
        Returns the amount to transfer.
        :return: webelement
        """
        return self._driver.find_element(*TransferPage.amount)

    def get_source_accounts(self) -> WebElement:
        """
        Returns the source account dropdown list.
        :return: webelement
        """
        return self._driver.find_element(*TransferPage.source_account)

    def get_target_accounts(self) -> WebElement:
        """
        Returns the target account dropdown list.
        :return: webelement
        """
        return self._driver.find_element(*TransferPage.target_account)

    def get_transfer_button(self) -> WebElement:
        """
        Returns the transfer button.
        :return: webelement
        """
        return self._driver.find_element(*TransferPage.transfer_button)

    def get_transfer_complete(self) -> WebElement:
        """
        Returns the transfer complete message.
        :return: webelement
        """
        return self._driver.find_element(*TransferPage.transfer_complete)

    def get_amount_result(self) -> WebElement:
        """
        Returns the amount of the completed transfer.
        :return: webelement
        """
        return self._driver.find_element(*TransferPage.amount_result)

    def get_source_account_result(self) -> WebElement:
        """
        Returns the source account of the completed transfer.
        :return: webelement
        """
        return self._driver.find_element(*TransferPage.source_account_result)

    def get_target_account_result(self) -> WebElement:
        """
        Returns the target account of the completed transfer.
        :return: webelement
        """
        return self._driver.find_element(*TransferPage.target_account_result)

    def get_amount_errors(self) -> WebElement:
        """
        Returns the amount errors.
        :return: webelement
        """
        return self._driver.find_element(*TransferPage.amount_errors)