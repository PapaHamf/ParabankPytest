from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

class FindTransactionPage():
    driver: Chrome

    # Declaring the page objects (fields & buttons)
    account_number: tuple = (By.ID, "accountId")
    transaction_id: tuple = (By.ID, "transactionId")
    find_by_id_button: tuple = (By.ID, "findById")
    transaction_date: tuple = (By.ID, "transactionDate")
    find_by_date_button: tuple = (By.ID, "findByDate")
    transaction_from_date: tuple = (By.ID, "fromDate")
    transaction_to_date: tuple = (By.ID, "toDate")
    find_by_date_range_button: tuple = (By.ID, "findByDateRange")
    transaction_amount: tuple = (By.ID, "amount")
    find_by_amount_button: tuple = (By.ID, "findByAmount")

    # Declaring the error labels
    transaction_id_error: tuple = (By.ID, "transactionIdError")
    transaction_date_error: tuple = (By.ID, "transactionDateError")
    transaction_date_range_error: tuple = (By.ID, "dateRangeError")
    transaction_amount_error: tuple = (By.ID, "amountError")

    def __init__(self, driver):
        self._driver = driver

    def get_account_number(self):
        """
        Returns the account number field.
        :return: webelement
        """
        return self._driver.find_element(*FindTransactionPage.account_number)

    def get_transaction_id(self):
        """
        Returns the transaction identifier field.
        :return: webelement
        """
        return self._driver.find_element(*FindTransactionPage.transaction_id)

    def get_find_by_id_button(self):
        """
        Returns the find by identifier button.
        :return: webelement
        """
        return self._driver.find_element(*FindTransactionPage.find_by_id_button)

    def get_transaction_date(self):
        """
        Returns the transaction date field.
        :return: webelement
        """
        return self._driver.find_element(*FindTransactionPage.transaction_date)

    def get_find_by_date_button(self):
        """
        Returns the find by date button.
        :return: webelement
        """
        return self._driver.find_element(*FindTransactionPage.find_by_date_button)

    def get_transaction_from_date(self):
        """
        Returns the transaction from date field.
        :return: webelement
        """
        return self._driver.find_element(*FindTransactionPage.transaction_from_date)

    def get_transaction_to_date(self):
        """
        Returns the transaction to date field.
        :return: webelement
        """
        return self._driver.find_element(*FindTransactionPage.transaction_to_date)

    def get_find_by_date_range_button(self):
        """
        Returns the find by date range button.
        :return: webelement
        """
        return self._driver.find_element(*FindTransactionPage.find_by_date_range_button)

    def get_transaction_amount(self):
        """
        Returns the transaction amount field.
        :return: webelement
        """
        return self._driver.find_element(*FindTransactionPage.transaction_amount)

    def get_find_by_amount_button(self):
        """
        Returns the find by amount button.
        :return: webelement
        """
        return self._driver.find_element(*FindTransactionPage.find_by_amount_button)

    def get_transaction_id_error(self):
        """
        Returns the transaction identifier field error text.
        :return: webelement
        """
        return self._driver.find_element(*FindTransactionPage.transaction_id_error)

    def get_transaction_date_error(self):
        """
        Returns the transaction date field error text.
        :return: webelement
        """
        return self._driver.find_element(*FindTransactionPage.transaction_date_error)

    def get_transaction_date_range_error(self):
        """
        Returns the transaction date range fields error text.
        :return: webelement
        """
        return self._driver.find_element(*FindTransactionPage.transaction_date_range_error)

    def get_transaction_amount_error(self):
        """
        Returns the transaction amount field error text.
        :return: webelement
        """
        return self._driver.find_element(*FindTransactionPage.transaction_amount_error)