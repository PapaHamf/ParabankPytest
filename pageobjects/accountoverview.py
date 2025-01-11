from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

class OpenAccountPage():
    driver: Chrome

    # Declaring the page objects (fields & buttons)
    table_head: tuple = (By.TAG_NAME, "thead")
    table_rows: tuple = (By.TAG_NAME, "tr")
    account_number: tuple = (By.XPATH, "//td[1]")
    account_balance: tuple = (By.XPATH, "//td[2]")
    avaiable_amount: tuple = (By.XPATH, "//td[3]")
    total_amount: tuple = (By.XPATH)

    def __init__(self, driver):
        self._driver = driver