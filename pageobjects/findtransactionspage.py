from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from pageobjects.basepage import BasePage

class FindTransactionPage(BasePage):
    """
    Class that holds the locators of the Find transactions page and methods to get its webelements.
    """
    driver: Chrome

    # Declaring the page objects (fields & buttons)
    ACCOUNT_LIST: tuple = (By.ID, "accountId")
    ACCOUNT_NUMBERS: tuple = (By.TAG_NAME, "option")
    TRANSACTION_ID: tuple = (By.ID, "transactionId")
    FIND_BY_ID_BUTTON: tuple = (By.ID, "findById")
    TRANSACTION_DATE: tuple = (By.ID, "transactionDate")
    FIND_BY_DATE_BUTTON: tuple = (By.ID, "findByDate")
    TRANSACTION_FROM_DATE: tuple = (By.ID, "fromDate")
    TRANSACTION_TO_DATE: tuple = (By.ID, "toDate")
    FIND_BY_DATE_RANGE_BUTTON: tuple = (By.ID, "findByDateRange")
    TRANSACTION_AMOUNT: tuple = (By.ID, "amount")
    FIND_BY_AMOUNT_BUTTON: tuple = (By.ID, "findByAmount")
    RESULTS_TABLE: tuple = (By.ID, "transactionTable")
    RESULTS_ROW: tuple = (By.CSS_SELECTOR, "tbody tr")

    # Declaring the error labels
    ERROR_BLOCK: tuple = (By.ID, "errorContainer")
    TRANSACTION_ID_ERROR: tuple = (By.ID, "transactionIdError")
    TRANSACTION_DATE_ERROR: tuple = (By.ID, "transactionDateError")
    TRANSACTION_DATE_RANGE_ERROR: tuple = (By.ID, "dateRangeError")
    TRANSACTION_AMOUNT_ERROR: tuple = (By.ID, "amountError")

    def __init__(self, driver):
        self._driver = driver

    def get_account_list(self) -> WebElement:
        """
        Returns the account list.
        :return: webelement
        """
        return self._driver.find_element(*FindTransactionPage.ACCOUNT_LIST)

    def get_account_numbers(self) -> list[WebElement]:
        """
        Returns the account numbers list.
        :return: webelement
        """
        accounts_list = self.get_account_list()
        return accounts_list.find_elements(*FindTransactionPage.ACCOUNT_NUMBERS)

    def get_transaction_id(self) -> WebElement:
        """
        Returns the transaction identifier field.
        :return: webelement
        """
        return self._driver.find_element(*FindTransactionPage.TRANSACTION_ID)

    def get_find_by_id_button(self) -> WebElement:
        """
        Returns the find by identifier button.
        :return: webelement
        """
        return self._driver.find_element(*FindTransactionPage.FIND_BY_ID_BUTTON)

    def get_transaction_date(self) -> WebElement:
        """
        Returns the transaction date field.
        :return: webelement
        """
        return self._driver.find_element(*FindTransactionPage.TRANSACTION_DATE)

    def get_find_by_date_button(self) -> WebElement:
        """
        Returns the find by date button.
        :return: webelement
        """
        return self._driver.find_element(*FindTransactionPage.FIND_BY_DATE_BUTTON)

    def get_transaction_from_date(self) -> WebElement:
        """
        Returns the transaction from date field.
        :return: webelement
        """
        return self._driver.find_element(*FindTransactionPage.TRANSACTION_FROM_DATE)

    def get_transaction_to_date(self) -> WebElement:
        """
        Returns the transaction to date field.
        :return: webelement
        """
        return self._driver.find_element(*FindTransactionPage.TRANSACTION_TO_DATE)

    def get_find_by_date_range_button(self) -> WebElement:
        """
        Returns the find by date range button.
        :return: webelement
        """
        return self._driver.find_element(*FindTransactionPage.FIND_BY_DATE_RANGE_BUTTON)

    def get_transaction_amount(self) -> WebElement:
        """
        Returns the transaction amount field.
        :return: webelement
        """
        return self._driver.find_element(*FindTransactionPage.TRANSACTION_AMOUNT)

    def get_find_by_amount_button(self) -> WebElement:
        """
        Returns the find by amount button.
        :return: webelement
        """
        return self._driver.find_element(*FindTransactionPage.FIND_BY_AMOUNT_BUTTON)

    def get_results_table(self) -> WebElement:
        """
        Returns the results table.
        :return: webelement
        """
        return self._driver.find_element(*FindTransactionPage.RESULTS_TABLE)

    def get_results_transactions(self) -> list[WebElement]:
        """
        Returns the results rows.
        :return: webelement
        """
        table = self.get_results_table()
        return table.find_elements(*FindTransactionPage.RESULTS_ROW)

    def get_error_message(self) -> WebElement:
        """
        Returns the internal error message text.
        :return: webelement
        """
        return self._driver.find_element(*FindTransactionPage.TRANSACTION_ID_ERROR)

    def get_transaction_id_error(self) -> WebElement:
        """
        Returns the transaction identifier field error text.
        :return: webelement
        """
        return self._driver.find_element(*FindTransactionPage.TRANSACTION_ID_ERROR)

    def get_transaction_date_error(self) -> WebElement:
        """
        Returns the transaction date field error text.
        :return: webelement
        """
        return self._driver.find_element(*FindTransactionPage.TRANSACTION_DATE_ERROR)

    def get_transaction_date_range_error(self) -> WebElement:
        """
        Returns the transaction date range fields error text.
        :return: webelement
        """
        return self._driver.find_element(*FindTransactionPage.TRANSACTION_DATE_RANGE_ERROR)

    def get_transaction_amount_error(self) -> WebElement:
        """
        Returns the transaction amount field error text.
        :return: webelement
        """
        return self._driver.find_element(*FindTransactionPage.TRANSACTION_AMOUNT_ERROR)