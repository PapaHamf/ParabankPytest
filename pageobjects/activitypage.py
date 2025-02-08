from selenium.common import NoSuchElementException
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

class ActivityPage():
    driver: Chrome

    # Declaring the page objects (fields & buttons)
    account_number: tuple = (By.ID, "accountId")
    account_type: tuple = (By.ID, "accountType")
    account_balance: tuple = (By.ID, "balance")
    available_amount: tuple = (By.ID, "availableBalance")
    activity_period: tuple = (By.ID, "month")
    activity_type: tuple = (By.ID, "transactionType")
    activity_button: tuple = (By.CSS_SELECTOR, "input[value='Go']")
    transactions_table: tuple = (By.ID, "transactionTable")
    # Allows to skip the thead tag
    transactions_rows: tuple = (By.CSS_SELECTOR, "tbody tr")
    # Chaining does not work w/ XPATH locators...
    transaction_dates: tuple = (By.CSS_SELECTOR, "tr td:nth-child(1)")
    transaction_names: tuple = (By.CSS_SELECTOR, "tr td:nth-child(2)")
    transaction_debits: tuple = (By.CSS_SELECTOR, "tr td:nth-child(3)")
    transaction_credits: tuple = (By.CSS_SELECTOR, "tr td:nth-child(4)")
    transaction_link: tuple = (By.TAG_NAME, "a")
    no_transactions: tuple = (By.ID, "noTransactions")

    def __init__(self, driver):
        self._driver = driver

    def get_account_number(self) -> WebElement:
        """
        Returns the account number.
        :return: webelement
        """
        return self._driver.find_element(*ActivityPage.account_number)

    def get_account_type(self) -> WebElement:
        """
        Returns the account type.
        :return: webelement
        """
        return self._driver.find_element(*ActivityPage.account_type)

    def get_account_balance(self) -> WebElement:
        """
        Returns the account balance.
        :return: webelement
        """
        return self._driver.find_element(*ActivityPage.account_balance)

    def get_available_amount(self) -> WebElement:
        """
        Returns the account available amount.
        :return: webelement
        """
        return self._driver.find_element(*ActivityPage.available_amount)

    def get_activity_period(self) -> WebElement:
        """
        Returns the activity (transactions) period dropdown list.
        :return: webelement
        """
        return self._driver.find_element(*ActivityPage.activity_period)

    def get_activity_type(self) -> WebElement:
        """
        Returns the activity (transactions) type dropdown list.
        :return: webelement
        """
        return self._driver.find_element(*ActivityPage.activity_type)

    def get_activity_button(self) -> WebElement:
        """
        Returns the activity (transactions) display button.
        :return: webelement
        """
        return self._driver.find_element(*ActivityPage.activity_button)

    def get_transaction_table(self) -> WebElement:
        """
        Returns the full transactions table.
        :return: webelement
        """
        return self._driver.find_element(*ActivityPage.transactions_table)

    def get_transaction_dates(self) -> WebElement:
        """
        Returns the transactions dates list or the no transactions message.
        :return: webelement
        """
        self._table = self.get_transaction_table()
        try:
            return self._table.find_elements(*ActivityPage.transaction_dates)
        except NoSuchElementException:
            return self.get_no_transactions()


    def get_transaction_names(self) -> WebElement:
        """
        Returns the transactions names list or the no transactions message.
        :return: webelement
        """
        self._table = self.get_transaction_table()
        try:
            return self._table.find_elements(*ActivityPage.transaction_names)
        except NoSuchElementException:
            return self.get_no_transactions()

    def get_transaction_debits(self) -> WebElement:
        """
        Returns the transactions debits amount list or the no transactions message.
        :return: webelement
        """
        self._table = self.get_transaction_table()
        try:
            return self._table.find_elements(*ActivityPage.transaction_debits)
        except NoSuchElementException:
            return self.get_no_transactions()

    def get_transaction_credits(self) -> WebElement:
        """
        Returns the transactions credits amount list or the no transactions message.
        :return: webelement
        """
        try:
            return self._table.find_elements(*ActivityPage.transaction_credits)
        except NoSuchElementException:
            return self.get_no_transactions()

    def get_transaction_link_by_text(self, text: str) -> WebElement:
        """
        Returns the transactions link using the text description.
        :param text: Text describing the transaction name.
        :return: webelement
        """
        self._table = self.get_transaction_table()
        rows = self._table.find_elements(*ActivityPage.transactions_rows)
        for row in rows:
            trans_link = row.find_element(*ActivityPage.transaction_link)
            if text in trans_link.text:
                return trans_link

    def get_transaction_debit_by_name(self, text: str) -> WebElement:
        """
        Returns the transactions debit amount using the text description.
        :param text: Text describing the transaction name.
        :return: webelement
        """
        self._table = self.get_transaction_table()
        rows = self._table.find_elements(*ActivityPage.transactions_rows)
        for row in rows:
            trans_link = row.find_element(*ActivityPage.transaction_link)
            if text in trans_link.text:
                return row.find_element(*ActivityPage.transaction_debits)

    def get_transaction_credit_by_name(self, text: str) -> WebElement:
        """
        Returns the transactions credit amount using the text description.
        :param text: Text describing the transaction name.
        :return: webelement
        """
        self._table = self.get_transaction_table()
        rows = self._table.find_elements(*ActivityPage.transactions_rows)
        for row in rows:
            trans_link = row.find_element(*ActivityPage.transaction_link)
            if text in trans_link.text:
                return row.find_element(*ActivityPage.transaction_credits)

    def get_no_transactions(self) -> WebElement:
        """
        Returns the no transactions message.
        :return: webelement
        """
        return self._driver.find_element(*ActivityPage.no_transactions)