import re

from selenium.common import NoSuchElementException
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from pageobjects.basepage import BasePage

class ActivityPage(BasePage):
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

    # Declaring the success and error messages
    VALID_PAGE_TITLE_POSITIVE = "ParaBank | Account Activity"
    FUNDS_SENT = "Funds Transfer Sent"
    FUNDS_RECEIVED = "Funds Transfer Received"

    def __init__(self, driver):
        self._driver = driver

    def get_account_number(self) -> WebElement:
        """
        Returns the account number.
        :return: webelement
        """
        return self.verify_element_presence(ActivityPage.ACCOUNT_NUMBER)

    def get_account_type(self) -> WebElement:
        """
        Returns the account type.
        :return: webelement
        """
        return self.verify_element_presence(ActivityPage.ACCOUNT_TYPE)

    def get_account_balance(self) -> WebElement:
        """
        Returns the account balance.
        :return: webelement
        """
        return self.verify_element_presence(ActivityPage.ACCOUNT_BALANCE)

    def get_available_amount(self) -> WebElement:
        """
        Returns the account available amount.
        :return: webelement
        """
        return self.verify_element_presence(ActivityPage.AVAILABLE_AMOUNT)

    def get_activity_period(self) -> WebElement:
        """
        Returns the activity (transactions) period dropdown list.
        :return: webelement
        """
        return self.verify_element_presence(ActivityPage.ACTIVITY_PERIOD)

    def get_activity_type(self) -> WebElement:
        """
        Returns the activity (transactions) type dropdown list.
        :return: webelement
        """
        return self.verify_element_presence(ActivityPage.ACTIVITY_TYPE)

    def get_activity_button(self) -> WebElement:
        """
        Returns the activity (transactions) display button.
        :return: webelement
        """
        return self.verify_element_presence(ActivityPage.ACTIVITY_BUTTON)

    def get_transaction_table(self) -> WebElement:
        """
        Returns the full transactions table.
        :return: webelement
        """
        return self.verify_element_presence(ActivityPage.TRANSACTIONS_TABLE)

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
        self._table = self.get_transaction_table()
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
        self._rows = self._table.find_elements(*ActivityPage.TRANSACTIONS_ROWS)
        for row in self._rows:
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
        self._rows = self._table.find_elements(*ActivityPage.TRANSACTIONS_ROWS)
        for row in self._rows:
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
        self._rows = self._table.find_elements(*ActivityPage.TRANSACTIONS_ROWS)
        for row in self._rows:
            trans_link = row.find_element(*ActivityPage.TRANSACTION_LINK)
            if text in trans_link.text:
                return row.find_element(*ActivityPage.TRANSACTION_CREDITS)

    def get_transaction_by_name(self, text: str) -> list[str]:
        """
        Returns the transaction row using the text description.
        :param text: Text describing the transaction name.
        :return:
        """
        pass

    def get_transaction_by_index(self, index: int) -> list[str]:
        """
        Returns the transaction row using the text description.
        :param index: List index of the transaction.
        :return:
        """
        self._row = []
        self._table = self.get_transaction_table()
        self._temp = self._table.find_elements(*ActivityPage.TRANSACTIONS_ROWS)[index]
        try:
            self._row.append(self._temp.find_element(*ActivityPage.TRANSACTION_DATES).text)
        except NoSuchElementException:
            self._row.append("")
        try:
            self._row.append(self._temp.find_element(*ActivityPage.TRANSACTION_NAMES).text)
        except NoSuchElementException:
            self._row.append("")
        try:
            self._row.append(float(re.sub(r"[^0-9.]", "",
                                          self._temp.find_element(*ActivityPage.TRANSACTION_DEBITS).text)))
        except (NoSuchElementException, ValueError):
            self._row.append("")
        try:
            self._row.append(float(re.sub(r"[^0-9.]", "",
                                          self._temp.find_element(*ActivityPage.TRANSACTION_CREDITS).text)))
        except (NoSuchElementException, ValueError):
            self._row.append("")
        return self._row

    def get_no_transactions(self) -> WebElement:
        """
        Returns the no transactions message.
        :return: webelement
        """
        return self._driver.find_element(*ActivityPage.NO_TRANSACTION)