from selenium.common import NoSuchElementException
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.remote.webelement import WebElement

from pageobjects.basepage import BasePage

class AccountOverview(BasePage):
    """
    Class that holds the locators of the Account overview page and methods to get its webelements.
    """
    driver: Chrome

    # Declaring the page objects (fields & buttons)
    TABLE_HEAD: tuple = (By.TAG_NAME, "thead")
    TABLE_ROWS: tuple = (By.TAG_NAME, "tr")
    # Re-used to get the single account number
    # Does not work: change to //td/a, rename this one to ACCOUNT_NUMBER
    ACCOUNT_NUMBERS: tuple = (By.XPATH, "//td[1]/a")
    ACCOUNT_NUMBER: tuple = (By.XPATH, "//td[1]")
    # Re-used to get the single account balance
    ACCOUNT_BALANCES: tuple = (By.XPATH, "//td[2]")
    ACCOUNT_LINK: tuple = (By.TAG_NAME, "a")
    AVAILABLE_AMOUNTS: tuple = (By.XPATH, "//td[3]")
    # locate_with accepts the dictionary!
    TOTAL_TEXT: dict = {By.XPATH: "//td/b[text()='Total']"}
    TOTAL_AMOUNT: tuple = (By.TAG_NAME, "b")

    def __init__(self, driver):
        self._driver = driver

    def get_table_head(self) -> WebElement:
        """
        Returns the table header.
        :return: webelement
        """
        return self.verify_element_presence(AccountOverview.TABLE_HEAD)

    def get_table_rows(self) -> list[WebElement]:
        """
        Returns all table rows.
        :return: webelement
        """
        return self.verify_elements_presence(AccountOverview.TABLE_ROWS)

    def get_account_numbers(self) -> list[WebElement]:
        """
        Returns all cells with the account numbers list.
        :return: webelement
        """
        return self.verify_elements_presence(AccountOverview.ACCOUNT_NUMBERS)

    def get_account_numbers_text(self) -> list:
        """
        Returns the account numbers list as strings.
        :return:
        """
        return self.get_elements_texts(self.get_account_numbers())

    def get_account_balances(self) -> list[WebElement]:
        """
        Returns all cells with the account balances list.
        :return: webelement
        """
        return self.verify_elements_presence(AccountOverview.ACCOUNT_BALANCES)

    def get_account_balances_texts(self) -> list[str]:
        """
        Returns the account balances list as strings
        :return:
        """
        balances = self.get_elements_texts(self.get_account_balances())
        # Removes the total amount from the list
        balances.pop()
        return balances

    def get_account_balances_numbers(self) -> list[float]:
        """
        Returns the account balances list as float values.
        :return:
        """
        balances = self.get_elements_numbers(self.get_account_balances())
        # Removes the total amount from the list
        balances.pop()
        return balances

    def get_available_amounts(self) -> list[WebElement]:
        """
        Returns all cells with the available amounts list.
        :return: webelement
        """
        return self.verify_elements_presence(AccountOverview.AVAILABLE_AMOUNTS)

    def get_available_amounts_numbers(self) -> list:
        """
        Returns the available amounts list as float values.
        :return:
        """
        return self.get_elements_numbers(self.get_available_amounts())

    def get_total_amount(self) -> WebElement:
        """
        Returns the total amount field.
        :return: webelement
        """
        return self._driver.find_element(locate_with(*AccountOverview.TOTAL_AMOUNT).to_right_of(AccountOverview.TOTAL_TEXT))

    def get_account_balance(self, account_number: str) -> WebElement:
        """
        Returns the given account balance.
        :param account_number: The number of the account which balance should be returned.
        :return: webelement
        """
        rows = self.get_table_rows()
        for row in rows:
            try:
                acc_no = row.find_element(*AccountOverview.ACCOUNT_LINK)
            except NoSuchElementException:
                continue
            if acc_no.text == account_number:
                return row.find_element(*AccountOverview.ACCOUNT_BALANCES)

    def get_available_amount(self, account_number: str) -> WebElement:
        """
        Returns the given account available amount.
        :param account_number: The number of the account which available amount should be returned.
        :return: webelement
        """
        rows = self.get_table_rows()
        for row in rows:
            try:
                acc_no = row.find_element(*AccountOverview.ACCOUNT_LINK)
            except NoSuchElementException:
                continue
            if acc_no.text == account_number:
                return row.find_element(*AccountOverview.AVAILABLE_AMOUNTS)



