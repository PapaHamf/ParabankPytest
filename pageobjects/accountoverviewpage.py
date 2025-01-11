from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with

class AccountOverview():
    driver: Chrome

    # Declaring the page objects (fields & buttons)
    table_head: tuple = (By.TAG_NAME, "thead")
    table_rows: tuple = (By.TAG_NAME, "tr")
    account_number: tuple = (By.XPATH, "//td[1]")
    account_balance: tuple = (By.XPATH, "//td[2]")
    avaiable_amount: tuple = (By.XPATH, "//td[3]")
    total_text: tuple = (By.XPATH, "//td/b[text()='Total'])
    total_amount: tuple = (By.TAG_NAME, "b")

    def __init__(self, driver):
        self._driver = driver

    def get_table_head(self):
        """
        Returns the table header.
        :return: webelement
        """
        return self._driver.find_element(*AccountOverview.table_head)

    def get_table_rows(self):
        """
        Returns the all table rows.
        :return: webelement
        """
        return self._driver.find_elements(*AccountOverview.table_rows)

    def