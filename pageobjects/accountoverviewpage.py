from selenium.common import NoSuchElementException
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.remote.webelement import WebElement

class AccountOverview():
    driver: Chrome

    # Declaring the page objects (fields & buttons)
    table_head: tuple = (By.TAG_NAME, "thead")
    table_rows: tuple = (By.TAG_NAME, "tr")
    # Re-used to get the single account number
    # Does not work: change to //td/a, rename this one to account_number
    account_numbers: tuple = (By.XPATH, "//td[1]/a")
    account_number: tuple = (By.XPATH, "//td[1]")
    # Re-used to get the single account balance
    account_balances: tuple = (By.XPATH, "//td[2]")
    account_link: tuple = (By.TAG_NAME, "a")
    available_amounts: tuple = (By.XPATH, "//td[3]")
    # locate_with accepts the dictionary!
    total_text: dict = {By.XPATH: "//td/b[text()='Total']"}
    total_amount: tuple = (By.TAG_NAME, "b")

    def __init__(self, driver):
        self._driver = driver

    def get_table_head(self) -> WebElement:
        """
        Returns the table header.
        :return: webelement
        """
        return self._driver.find_element(*AccountOverview.table_head)

    def get_table_rows(self) -> WebElement:
        """
        Returns all table rows.
        :return: webelement
        """
        return self._driver.find_elements(*AccountOverview.table_rows)

    def get_account_numbers(self) -> WebElement:
        """
        Returns all cells with the account numbers list.
        :return: webelement
        """
        return self._driver.find_elements(*AccountOverview.account_numbers)

    def get_account_balances(self) -> WebElement:
        """
        Returns all cells with the account balances list.
        :return: webelement
        """
        return self._driver.find_elements(*AccountOverview.account_balances)

    def get_available_amounts(self) -> WebElement:
        """
        Returns all cells with the available amounts list.
        :return: webelement
        """
        return self._driver.find_elements(*AccountOverview.available_amounts)

    def get_total_amount(self) -> WebElement:
        """
        Returns the total amount field.
        :return: webelement
        """
        return self._driver.find_element(locate_with(*AccountOverview.total_amount).to_right_of(AccountOverview.total_text))

    def get_account_balance(self, account_number: str) -> WebElement:
        """
        Returns the given account balance.
        :param account_number: The number of the account which balance should be returned.
        :return: webelement
        """
        rows = self.get_table_rows()
        for row in rows:
            try:
                acc_no = row.find_element(*AccountOverview.account_link)
            except NoSuchElementException:
                continue
            if acc_no.text == account_number:
                return row.find_element(*AccountOverview.account_balances)

    def get_available_amount(self, account_number: str) -> WebElement:
        """
        Returns the given account available amount.
        :param account_number: The number of the account which available amount should be returned.
        :return: webelement
        """
        rows = self.get_table_rows()
        for row in rows:
            try:
                acc_no = row.find_element(*AccountOverview.account_link)
            except NoSuchElementException:
                continue
            if acc_no.text == account_number:
                return row.find_element(*AccountOverview.available_amounts)



