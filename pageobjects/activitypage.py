from selenium.common import NoSuchElementException
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

class ActivityPage():
    """
    Class that holds the locators of the Activity page and methods to get its webelements.
    """
    driver: Chrome

    # Declaring the page objects (fields & buttons)
    ACCOUNT_NUMBER: tuple = (By.ID, "accountId")
    ACCOUNT_TYPE: tuple = (By.ID, "accountType")
    ACCOUNT_BALANCE: tuple = (By.ID, "balance")
    AVAILABLE_AMOUNT: tuple = (By.ID, "availableBalance")
    ACTIVITY_PERIOD: tuple = (By.ID, "month")
    ACTIVITY_TYPE: tuple = (By.ID, "transactionType")
    ACTIVITY_BUTTON: tuple = (By.CSS_SELECTOR, "input[value='Go']")
    TRANSACTIONS_TABLE: tuple = (By.ID, "transactionTable")
    # Allows to skip the thead tag
    TRANSACTIONS_ROWS: tuple = (By.CSS_SELECTOR, "tbody tr")
    # Chaining does not work w/ XPATH locators...
    TRANSACTION_DATES: tuple = (By.CSS_SELECTOR, "tr td:nth-child(1)")
    TRANSACTION_NAMES: tuple = (By.CSS_SELECTOR, "tr td:nth-child(2)")
    TRANSACTION_DEBITS: tuple = (By.CSS_SELECTOR, "tr td:nth-child(3)")
    TRANSACTION_CREDITS: tuple = (By.CSS_SELECTOR, "tr td:nth-child(4)")
    TRANSACTION_LINK: tuple = (By.TAG_NAME, "a")
    NO_TRANSACTION: tuple = (By.ID, "noTransactions")

    def __init__(self, driver):
        self._driver = driver

    def get_account_number(self) -> WebElement:
        """
        Returns the account number.
        :return: webelement
        """
        return self._driver.find_element(*ActivityPage.ACCOUNT_NUMBER)

    def get_account_type(self) -> WebElement:
        """
        Returns the account type.
        :return: webelement
        """
        return self._driver.find_element(*ActivityPage.ACCOUNT_TYPE)

    def get_account_balance(self) -> WebElement:
        """
        Returns the account balance.
        :return: webelement
        """
        return self._driver.find_element(*ActivityPage.ACCOUNT_BALANCE)

    def get_available_amount(self) -> WebElement:
        """
        Returns the account available amount.
        :return: webelement
        """
        return self._driver.find_element(*ActivityPage.AVAILABLE_AMOUNT)

    def get_activity_period(self) -> WebElement:
        """
        Returns the activity (transactions) period dropdown list.
        :return: webelement
        """
        return self._driver.find_element(*ActivityPage.ACTIVITY_PERIOD)

    def get_activity_type(self) -> WebElement:
        """
        Returns the activity (transactions) type dropdown list.
        :return: webelement
        """
        return self._driver.find_element(*ActivityPage.ACTIVITY_TYPE)

    def get_activity_button(self) -> WebElement:
        """
        Returns the activity (transactions) display button.
        :return: webelement
        """
        return self._driver.find_element(*ActivityPage.ACTIVITY_BUTTON)

    def get_transaction_table(self) -> WebElement:
        """
        Returns the full transactions table.
        :return: webelement
        """
        return self._driver.find_element(*ActivityPage.TRANSACTIONS_TABLE)

    def get_transaction_dates(self) -> WebElement | list[WebElement]:
        """
        Returns the transactions dates list or the no transactions message.
        :return: webelement
        """
        self._table = self.get_transaction_table()
        try:
            return self._table.find_elements(*ActivityPage.TRANSACTION_DATES)
        except NoSuchElementException:
            return self.get_no_transactions()


    def get_transaction_names(self) -> WebElement | list[WebElement]:
        """
        Returns the transactions names list or the no transactions message.
        :return: webelement
        """
        self._table = self.get_transaction_table()
        try:
            return self._table.find_elements(*ActivityPage.TRANSACTION_NAMES)
        except NoSuchElementException:
            return self.get_no_transactions()

    def get_transaction_debits(self) -> WebElement | list[WebElement]:
        """
        Returns the transactions debits amount list or the no transactions message.
        :return: webelement
        """
        self._table = self.get_transaction_table()
        try:
            return self._table.find_elements(*ActivityPage.TRANSACTION_DEBITS)
        except NoSuchElementException:
            return self.get_no_transactions()

    def get_transaction_credits(self) -> WebElement | list[WebElement]:
        """
        Returns the transactions credits amount list or the no transactions message.
        :return: webelement
        """
        try:
            return self._table.find_elements(*ActivityPage.TRANSACTION_CREDITS)
        except NoSuchElementException:
            return self.get_no_transactions()

    def get_transaction_link_by_text(self, text: str) -> WebElement:
        """
        Returns the transactions link using the text description.
        :param text: Text describing the transaction name.
        :return: webelement
        """
        self._table = self.get_transaction_table()
        rows = self._table.find_elements(*ActivityPage.TRANSACTIONS_ROWS)
        for row in rows:
            trans_link = row.find_element(*ActivityPage.TRANSACTION_LINK)
            if text in trans_link.text:
                return trans_link

    def get_transaction_debit_by_name(self, text: str) -> WebElement:
        """
        Returns the transactions debit amount using the text description.
        :param text: Text describing the transaction name.
        :return: webelement
        """
        self._table = self.get_transaction_table()
        rows = self._table.find_elements(*ActivityPage.TRANSACTIONS_ROWS)
        for row in rows:
            trans_link = row.find_element(*ActivityPage.TRANSACTION_LINK)
            if text in trans_link.text:
                return row.find_element(*ActivityPage.TRANSACTION_DEBITS)

    def get_transaction_credit_by_name(self, text: str) -> WebElement:
        """
        Returns the transactions credit amount using the text description.
        :param text: Text describing the transaction name.
        :return: webelement
        """
        self._table = self.get_transaction_table()
        rows = self._table.find_elements(*ActivityPage.TRANSACTIONS_ROWS)
        for row in rows:
            trans_link = row.find_element(*ActivityPage.TRANSACTION_LINK)
            if text in trans_link.text:
                return row.find_element(*ActivityPage.TRANSACTION_CREDITS)

    def get_no_transactions(self) -> WebElement:
        """
        Returns the no transactions message.
        :return: webelement
        """
        return self._driver.find_element(*ActivityPage.NO_TRANSACTION)