from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

class TransferPage():
    """
    Class that holds the locators of the Transfer page and methods to get its webelements.
    """
    driver: Chrome

    # Declaring the page objects (fields & buttons)
    AMOUNT: tuple = (By.ID, "amount")
    SOURCE_ACCOUNT: tuple = (By.ID, "fromAccountId")
    TARGET_ACCOUNT: tuple = (By.ID, "toAccountId")
    TRANSFER_BUTTON: tuple = (By.CSS_SELECTOR, "input[value='Transfer']")
    TRANSFER_COMPLETE: tuple = (By.XPATH, "//h1[text()='Transfer Complete!']")
    AMOUNT_RESULT: tuple = (By.ID, "amountResult")
    SOURCE_ACCOUNT_RESULT: tuple = (By.ID, "fromAccountIdResult")
    TARGET_ACCOUNT_RESULT: tuple = (By.ID, "toAccountIdResult")

    # Declaring the error labels
    # Possible values:
    # 1. The amount cannot be empty.
	# 2. Please enter a valid amount.
    AMOUNT_ERRORS: tuple = (By.ID, "amount.errors")
    # Probably not used
    INTERNAL_ERROR: tuple = (By.ID, "showError")

    def __init__(self, driver):
        self._driver = driver

    def get_amount(self) -> WebElement:
        """
        Returns the amount to transfer.
        :return: webelement
        """
        return self._driver.find_element(*TransferPage.AMOUNT)

    def get_source_accounts(self) -> WebElement:
        """
        Returns the source account dropdown list.
        :return: webelement
        """
        return self._driver.find_element(*TransferPage.SOURCE_ACCOUNT)

    def get_target_accounts(self) -> WebElement:
        """
        Returns the target account dropdown list.
        :return: webelement
        """
        return self._driver.find_element(*TransferPage.TARGET_ACCOUNT)

    def get_transfer_button(self) -> WebElement:
        """
        Returns the transfer button.
        :return: webelement
        """
        return self._driver.find_element(*TransferPage.TRANSFER_BUTTON)

    def get_transfer_complete(self) -> WebElement:
        """
        Returns the transfer complete message.
        :return: webelement
        """
        return self._driver.find_element(*TransferPage.TRANSFER_COMPLETE)

    def get_amount_result(self) -> WebElement:
        """
        Returns the amount of the completed transfer.
        :return: webelement
        """
        return self._driver.find_element(*TransferPage.AMOUNT_RESULT)

    def get_source_account_result(self) -> WebElement:
        """
        Returns the source account of the completed transfer.
        :return: webelement
        """
        return self._driver.find_element(*TransferPage.SOURCE_ACCOUNT_RESULT)

    def get_target_account_result(self) -> WebElement:
        """
        Returns the target account of the completed transfer.
        :return: webelement
        """
        return self._driver.find_element(*TransferPage.TARGET_ACCOUNT_RESULT)

    def get_amount_errors(self) -> WebElement:
        """
        Returns the amount errors.
        :return: webelement
        """
        return self._driver.find_element(*TransferPage.AMOUNT_ERRORS)