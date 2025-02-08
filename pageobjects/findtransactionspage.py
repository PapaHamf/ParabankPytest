from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

class FindTransactionPage():
    driver: Chrome

    # Declaring the page objects (fields & buttons)
    account_list: tuple = (By.ID, "accountId")
    account_numbers: tuple = (By.TAG_NAME, "option")
    transaction_id: tuple = (By.ID, "transactionId")
    find_by_id_button: tuple = (By.ID, "findById")
    transaction_date: tuple = (By.ID, "transactionDate")
    find_by_date_button: tuple = (By.ID, "findByDate")
    transaction_from_date: tuple = (By.ID, "fromDate")
    transaction_to_date: tuple = (By.ID, "toDate")
    find_by_date_range_button: tuple = (By.ID, "findByDateRange")
    transaction_amount: tuple = (By.ID, "amount")
    find_by_amount_button: tuple = (By.ID, "findByAmount")
    results_table: tuple = (By.ID, "transactionTable")
    results_row: tuple = (By.CSS_SELECTOR, "tbody tr")

    # Declaring the error labels
    error_block: tuple = (By.ID, "errorContainer")
    transaction_id_error: tuple = (By.ID, "transactionIdError")
    transaction_date_error: tuple = (By.ID, "transactionDateError")
    transaction_date_range_error: tuple = (By.ID, "dateRangeError")
    transaction_amount_error: tuple = (By.ID, "amountError")

    def __init__(self, driver):
        self._driver = driver

    def get_account_list(self) -> WebElement:
        """
        Returns the account list.
        :return: webelement
        """
        return self._driver.find_element(*FindTransactionPage.account_list)

    def get_account_numbers(self) -> WebElement:
        """
        Returns the account numbers list.
        :return: webelement
        """
        accounts_list = self.get_account_list()
        return accounts_list.find_elements(*FindTransactionPage.account_numbers)

    def get_transaction_id(self) -> WebElement:
        """
        Returns the transaction identifier field.
        :return: webelement
        """
        return self._driver.find_element(*FindTransactionPage.transaction_id)

    def get_find_by_id_button(self) -> WebElement:
        """
        Returns the find by identifier button.
        :return: webelement
        """
        return self._driver.find_element(*FindTransactionPage.find_by_id_button)

    def get_transaction_date(self) -> WebElement:
        """
        Returns the transaction date field.
        :return: webelement
        """
        return self._driver.find_element(*FindTransactionPage.transaction_date)

    def get_find_by_date_button(self) -> WebElement:
        """
        Returns the find by date button.
        :return: webelement
        """
        return self._driver.find_element(*FindTransactionPage.find_by_date_button)

    def get_transaction_from_date(self) -> WebElement:
        """
        Returns the transaction from date field.
        :return: webelement
        """
        return self._driver.find_element(*FindTransactionPage.transaction_from_date)

    def get_transaction_to_date(self) -> WebElement:
        """
        Returns the transaction to date field.
        :return: webelement
        """
        return self._driver.find_element(*FindTransactionPage.transaction_to_date)

    def get_find_by_date_range_button(self) -> WebElement:
        """
        Returns the find by date range button.
        :return: webelement
        """
        return self._driver.find_element(*FindTransactionPage.find_by_date_range_button)

    def get_transaction_amount(self) -> WebElement:
        """
        Returns the transaction amount field.
        :return: webelement
        """
        return self._driver.find_element(*FindTransactionPage.transaction_amount)

    def get_find_by_amount_button(self) -> WebElement:
        """
        Returns the find by amount button.
        :return: webelement
        """
        return self._driver.find_element(*FindTransactionPage.find_by_amount_button)

    def get_results_table(self) -> WebElement:
        """
        Returns the results table.
        :return: webelement
        """
        return self._driver.find_element(*FindTransactionPage.results_table)

    def get_results_transactions(self) -> list[WebElement]:
        """
       Returns the results rows.
       :return: webelement
       """
        table = self.get_results_table()
        return table.find_elements(*FindTransactionPage.results_row)

    def get_error_message(self) -> WebElement:
        """
        Returns the internal error message text.
        :return: webelement
        """
        return self._driver.find_element(*FindTransactionPage.transaction_id_error)

    def get_transaction_id_error(self) -> WebElement:
        """
        Returns the transaction identifier field error text.
        :return: webelement
        """
        return self._driver.find_element(*FindTransactionPage.transaction_id_error)

    def get_transaction_date_error(self) -> WebElement:
        """
        Returns the transaction date field error text.
        :return: webelement
        """
        return self._driver.find_element(*FindTransactionPage.transaction_date_error)

    def get_transaction_date_range_error(self) -> WebElement:
        """
        Returns the transaction date range fields error text.
        :return: webelement
        """
        return self._driver.find_element(*FindTransactionPage.transaction_date_range_error)

    def get_transaction_amount_error(self) -> WebElement:
        """
        Returns the transaction amount field error text.
        :return: webelement
        """
        return self._driver.find_element(*FindTransactionPage.transaction_amount_error)