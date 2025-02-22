from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

class AdminPage():
    """
    Class that holds the locators of the Administrator page and methods to get its webelements.
    """
    driver: Chrome

    # Declaring the page objects (fields & buttons)
    CLEAN_DB_BUTTON: tuple = (By.CSS_SELECTOR, "button[value='CLEAN']")
    INITIAL_BALANCE: tuple = (By.ID, "initialBalance")
    MINIMUM_BALANCE: tuple = (By.ID, "minimumBalance")
    DATA_ACCESS_MODE_SOAP: tuple = (By.ID, "accessMode1")
    DATA_ACCESS_MODE_RESTXML: tuple = (By.ID, "accessMode2")
    DATA_ACCESS_MODE_RESTJSON: tuple = (By.ID, "accessMode3")
    DATA_ACCESS_MODE_JDBC: tuple = (By.ID, "accessMode4")
    LOAN_PROVIDER: tuple = (By.ID, "loanProvider")
    LOAN_PROCESSOR: tuple = (By.ID, "loanProcessor")
    LOAN_THRESHOLD: tuple = (By.ID, "loanProcessorThreshold")
    SUBMIT_BUTTON: tuple = (By.ID, "Submit")

    def __init__(self, driver):
        self._driver = driver

    def get_clean_databas_button(self) -> WebElement:
        """
        Returns the clean database button.
        :return: webelement
        """
        return self._driver.find_element(*AdminPage.CLEAN_DB_BUTTON)

    def get_initial_balance(self) -> WebElement:
        """
        Returns the initial balance field.
        :return: webelement
        """
        return self._driver.find_element(*AdminPage.INITIAL_BALANCE)

    def get_minimum_balance(self) -> WebElement:
        """
        Returns the minimum balance field.
        :return: webelement
        """
        return self._driver.find_element(*AdminPage.MINIMUM_BALANCE)

    def get_access_mode_soap(self) -> WebElement:
        """
        Returns the access mode soap radio button.
        :return: webelement
        """
        return self._driver.find_element(*AdminPage.DATA_ACCESS_MODE_SOAP)

    def get_access_mode_restXML(self) -> WebElement:
        """
        Returns the access mode rest XML radio button.
        :return: webelement
        """
        return self._driver.find_element(*AdminPage.DATA_ACCESS_MODE_RESTXML)

    def get_access_mode_restJSON(self) -> WebElement:
        """
        Returns the access mode rest JSON radio button.
        :return: webelement
        """
        return self._driver.find_element(*AdminPage.DATA_ACCESS_MODE_RESTJSON)

    def get_access_mode_JDBC(self) -> WebElement:
        """
        Returns the access mode JDBC radio button.
        :return: webelement
        """
        return self._driver.find_element(*AdminPage.DATA_ACCESS_MODE_JDBC)

    def get_loan_provider(self) -> WebElement:
        """
        Returns the loan provider list.
        :return: webelement
        """
        return self._driver.find_element(*AdminPage.LOAN_PROVIDER)

    def get_loan_processor(self) -> WebElement:
        """
        Returns the loan processor list.
        :return: webelement
        """
        return self._driver.find_element(*AdminPage.LOAN_PROCESSOR)

    def get_loan_threshold(self) -> WebElement:
        """
        Returns the loan threshold field.
        :return: webelement
        """
        return self._driver.find_element(*AdminPage.LOAN_THRESHOLD)

    def get_submit_button(self) -> WebElement:
        """
        Returns the submit button.
        :return: webelement
        """
        return self._driver.find_element(*AdminPage.SUBMIT_BUTTON)


