from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

class AdminPage():
    """
    Class that holds the locators of the Administrator page and methods to get its webelements.
    """
    driver: Chrome

    # Declaring the page objects (fields & buttons)
    clean_db_button: tuple = (By.CSS_SELECTOR, "button[value='CLEAN']")
    initial_balance: tuple = (By.ID, "initialBalance")
    minimum_balance: tuple = (By.ID, "minimumBalance")
    data_access_mode_soap: tuple = (By.ID, "accessMode1")
    data_access_mode_restXML: tuple = (By.ID, "accessMode2")
    data_access_mode_restJSON: tuple = (By.ID, "accessMode3")
    data_access_mode_JDBC: tuple = (By.ID, "accessMode4")
    loan_provider: tuple = (By.ID, "loanProvider")
    loan_processor: tuple = (By.ID, "loanProcessor")
    loan_threshold: tuple = (By.ID, "loanProcessorThreshold")
    submit_button: tuple = (By.ID, "Submit")

    def __init__(self, driver):
        self._driver = driver

    def get_clean_database(self) -> WebElement:
        """
        Returns the clean database button.
        :return: webelement
        """
        return self._driver.find_element(*AdminPage.clean_db_button)

    def get_initial_balance(self) -> WebElement:
        """
        Returns the initial balance field.
        :return: webelement
        """
        return self._driver.find_element(*AdminPage.initial_balance)

    def get_minimum_balance(self) -> WebElement:
        """
        Returns the minimum balance field.
        :return: webelement
        """
        return self._driver.find_element(*AdminPage.minimum_balance)

    def get_access_mode_soap(self) -> WebElement:
        """
        Returns the access mode soap radio button.
        :return: webelement
        """
        return self._driver.find_element(*AdminPage.data_access_mode_soap)

    def get_access_mode_restXML(self) -> WebElement:
        """
        Returns the access mode rest XML radio button.
        :return: webelement
        """
        return self._driver.find_element(*AdminPage.data_access_mode_restXML)

    def get_access_mode_restJSON(self) -> WebElement:
        """
        Returns the access mode rest JSON radio button.
        :return: webelement
        """
        return self._driver.find_element(*AdminPage.data_access_mode_restJSON)

    def get_access_mode_JDBC(self) -> WebElement:
        """
        Returns the access mode JDBC radio button.
        :return: webelement
        """
        return self._driver.find_element(*AdminPage.data_access_mode_JDBC)

    def get_loan_provider(self) -> WebElement:
        """
        Returns the loan provider list.
        :return: webelement
        """
        return self._driver.find_element(*AdminPage.loan_provider)

    def get_loan_processor(self) -> WebElement:
        """
        Returns the loan processor list.
        :return: webelement
        """
        return self._driver.find_element(*AdminPage.loan_processor)

    def get_loan_threshold(self) -> WebElement:
        """
        Returns the loan threshold field.
        :return: webelement
        """
        return self._driver.find_element(*AdminPage.loan_threshold)

    def get_submit_button(self) -> WebElement:
        """
        Returns the submit button.
        :return: webelement
        """
        return self._driver.find_element(*AdminPage.submit_button)


