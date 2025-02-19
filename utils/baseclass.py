import logging
import inspect
import pytest

from faker import Faker
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from logging import Logger


class MyFaker(Faker):
    """
    Faker sub-class with couple of new methods especially w/ random numbers in names.
    """

    def name_with_random_no(self) -> str:
        """
        Returns random name with random number at the end.
        :return: string
        """
        return self.name() + str(int(self.randint(0, 1000)))

    def name_with_random_digits(self) -> str:
        """
        Returns random name with random numbers inside the name.
        :return: string
        """
        name: str = self.name()
        first: int = self.randint(0, len(name))
        return name[:first] + "".join([str(self.randint(0, 9)) for i in range(first, first + 3)]) + name[first+3:]

@pytest.mark.usefixtures("setup")
class BaseClass():
    """
    Base class for all of the test scenarios.
    """

    # Web pages constants (not used in tests, except HOMEPAGE)
    HOMEPAGE: str = "http://localhost:8000/parabank/"
    FORGOT_LOGIN: str = "http://localhost:8000/parabank/lookup.htm"
    REGISTER: str = "http://localhost:8000/parabank/register.htm"
    OPEN_ACCOUNT: str = "http://localhost:8000/parabank/openaccount.htm"
    ACCOUNT_OVERVIEW: str = "http://localhost:8000/parabank/overview.htm"
    # There is an argument ?id= that contains the account number
    ACTIVITY: str = "http://localhost:8000/parabank/activity.htm"
    # There is an argument ?id= that contains the transaction number
    TRANSACTION: str = "http://localhost:8000/parabank/transaction.htm"
    TRANSFER_FUNDS: str = "http://localhost:8000/parabank/transfer.htm"
    BILL_PAY: str = "http://localhost:8000/parabank/billpay.htm"
    FIND_TRANS: str = "http://localhost:8000/parabank/findtrans.htm"
    UPDATE_INFO: str = "http://localhost:8000/parabank/updateprofile.htm"
    REQUEST_LOAN: str = "http://localhost:8000/parabank/requestloan.htm"
    ADMIN_PAGE: str = "http://localhost:8000/parabank/admin.htm"
    CONTACT_FORM: str = "http://localhost:8000/parabank/contact.htm"

    def verify_element_presence(self, locator: str, timeout: int = 10) -> WebElement:
        """
        Verifies the web element presence on the page.
        :param locator: The locator whose presence is going to be checked. It should be in the XPATH format.
        :param timeout: The timeout for the explicit waiting. The default value is 10.
        :return: webelement
        """
        wait: WebDriverWait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.presence_of_element_located((By.XPATH, locator)))

    def get_list_values(self, dropdown_list: WebElement) -> list:
        """
        Returns the list of elements from the passed static dropdown (webelement).
        :param element: Webelement that references the static dropdown.
        :return: List of elements of the dropdown.
        """
        values = []
        for element in dropdown_list.find_elements(By.TAG_NAME, "option"):
            values.append(element.text)
        return values

    def select_value_from_dropdown_text(self, element: WebElement, text: str) -> None:
        """
        Selects the value from the passed list (webelement) using the text.
        :param element: Webelement that references the static dropdown.
        :param text: The text value to be selected.
        :return: None
        """
        dropdown: Select = Select(element)
        dropdown.select_by_visible_text(text)

    def select_value_from_dropdown_index(self, element: WebElement, index: int) -> None:
        """
        Selects the value from the passed list (webelement) using the index value.
        :param element: Webelement that references the static dropdown.
        :param index: The index value to be selected.
        :return: None
        """
        dropdown: Select = Select(element)
        dropdown.select_by_index(index)

    def get_logger(self, file_name: str = "logfile.log", level: str = "INFO") -> Logger:
        """
        Creates the logger object and defines the logging level.
        :param file_name: The file name of the log. The default value is logfile.log.
        :param level:  The logging level. The default value is INFO.
        :return: logger object
        """
        # Fixing the name of the file in the logs (otherwise it will be the name of the baseclass)
        logger_name = inspect.stack()[1][3]
        logger: Logger = logging.getLogger(logger_name)
        # Check if the logger already exits to avoid creating new logger in parametrized tests.
        if not len(logger.handlers):
            # Defining the log file
            file_handler = logging.FileHandler(file_name)
            # Defining the log format
            file_formater = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
            file_handler.setFormatter(file_formater)
            logger.addHandler(file_handler)
            # Setting the minimum level
            logger.setLevel(level)
        return logger

    def get_faker(self, locale: str = "pl_PL") -> Faker:
        """
        Creates the faker object with given locale and returns it.
        :param locale: Lets you define the locale of the fake data. Default value is pl_Pl.
        :return: faker object
        """
        return MyFaker(locale)
