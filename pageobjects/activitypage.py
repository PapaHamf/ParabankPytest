from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

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
    transaction_dates: tuple = (By.XPATH, "//td[1]")
    transaction_names: tuple = (By.XPATH, "//td[2]")
    transaction_debits: tuple = (By.XPATH, "//td[3]")
    transaction_credits: tuple = (By.XPATH, "//td[4]")
    transaction_link: tuple = (By.TAG_NAME, "a")
    no_transactions: tuple = (By.ID, "noTransactions")

    def __init__(self, driver):
        self._driver = driver

    def get_account_number(self):
        """
        Returns the account number.
        :return: webelement
        """
        return self._driver.find_element(*ActivityPage.account_number)

    def get_account_type(self):
        """
        Returns the account type.
        :return: webelement
        """
        return self._driver.find_element(*ActivityPage.activity_type)

    def get_account_balance(self):
        """
        Returns the account balance.
        :return: webelement
        """
        return self._driver.find_element(*ActivityPage.account_balance)

    def get_available_amount(self):
        """
        Returns the account available amount.
        :return: webelement
        """
        return self._driver.find_element(*ActivityPage.available_amount)

    def get_activity_period(self):
        """
        Returns the activity (transactions) period dropdown list.
        :return: webelement
        """
        return self._driver.find_element(*ActivityPage.activity_period)

    def get_activity_type(self):
        """
        Returns the activity (transactions) type dropdown list.
        :return: webelement
        """
        return self._driver.find_element(*ActivityPage.activity_type)

    def get_activity_button(self):
        """
        Returns the activity (transactions) display button.
        :return: webelement
        """
        return self._driver.find_element(*ActivityPage.activity_period)

    def get_transaction_table(self):
        """
        Returns the full transactions table.
        :return: webelement
        """
        return self._driver.find_element(*ActivityPage.transactions_table)

    def get_transaction_dates(self):
        """
        Returns the transactions dates list.
        :return: webelement
        """
        return self._driver.find_element(*ActivityPage.transaction_dates)

    def get_transaction_names(self):
        """
        Returns the transactions names list.
        :return: webelement
        """
        return self._driver.find_element(*ActivityPage.transaction_names)

    def get_transaction_debits(self):
        """
        Returns the transactions debits amount list.
        :return: webelement
        """
        return self._driver.find_element(*ActivityPage.transaction_debits)

    def get_transaction_credits(self):
        """
        Returns the transactions credits amount list.
        :return: webelement
        """
        return self._driver.find_element(*ActivityPage.transaction_credits)

    def get_transaction_link(self, text: str):
        """
        Returns the transactions link using the text description.
        :param text: Text describing the transaction name.
        :return: webelement
        """
        table = self.get_transaction_table()
        for row in table:
            trans_name = row.find_element(*ActivityPage.transaction_link)
            if text in trans_name.text:
                return trans_name

    def get_transaction_debit_by_name(self, text: str):
        """
        Returns the transactions debit amount using the text description.
        :param text: Text describing the transaction name.
        :return: webelement
        """
        table = self.get_transaction_table()
        for row in table:
            trans_name = row.find_element(*ActivityPage.transaction_link)
            if text in trans_name.text:
                return row.find_element(*ActivityPage.transaction_debits)

    def get_transaction_credit_by_name(self, text: str):
        """
        Returns the transactions credit amount using the text description.
        :param text: Text describing the transaction name.
        :return: webelement
        """
        table = self.get_transaction_table()
        for row in table:
            trans_name = row.find_element(*ActivityPage.transaction_link)
            if text in trans_name.text:
                return row.find_element(*ActivityPage.transaction_credits)

    def get_no_transactions(self):
        """
        Returns the no transactions message.
        :return: webelement
        """
        return self._driver.find_element(*ActivityPage.no_transactions)