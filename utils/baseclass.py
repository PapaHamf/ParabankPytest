import logging
import inspect
import pytest

from faker import Faker
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# List of to dos
# Implement sqlite3 database utilities (to log the test cases data)
# Implement JSON utilities (to write temporary data used in other cases)
# Implement Excel utilities (to inject some kind of data from outside)
# Implement the screenshot on failure feature (there is a plug-in)
# Implement the exception raising & catching utilities combined w/ the log.WARN (you can
# use the 'with pytest.raises(..) to catch the exceptions)
# Implement allure

class MyFaker(Faker):

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
class BaseClass:

    # Temporary constants
    # Move them to some config file (JSON or shelved binary?) or database?
    HOMEPAGE = "http://localhost:8000/parabank/"
    FORGOT_LOGIN = "http://localhost:8000/parabank/lookup.htm"
    REGISTER = "http://localhost:8000/parabank/register.htm"
    OPEN_ACCOUNT = "http://localhost:8000/parabank/openaccount.htm"
    ACCOUNT_OVERVIEW = "http://localhost:8000/parabank/overview.htm"
    ACTIVITY = "http://localhost:8000/parabank/activity.htm"
    # Should use it to assert the proper bill payment or transfers (seems like you can
    # transfer infinite amounts to the same account)
    # TRANSACTION = "http://localhost:8000/parabank/transaction.htm"
    TRANSFER_FUNDS = "http://localhost:8000/parabank/transfer.htm"
    BILL_PAY = "http://localhost:8000/parabank/billpay.htm"
    FIND_TRANS = "http://localhost:8000/parabank/findtrans.htm"
    UPDATE_INFO = "http://localhost:8000/parabank/updateprofile.htm"
    REQUEST_LOAN = "http://localhost:8000/parabank/requestloan.htm"

    def verify_element_presence(self, locator: str, timeout: int = 10) -> None:
        """
        Verifies the web element presence on the page.
        :param locator: The locator whose presence is going to be checked. It should be in the XPATH format.
        :param timeout: The timeout for the explicit waiting. The default value is 10.
        :return: None
        """
        wait = WebDriverWait(self.driver, timeout)
        wait.until(expected_conditions.presence_of_element_located((By.XPATH, locator)))

    def select_value_from_dropdown_text(self, element, text: str):
        """
        Selects the value from the passed list (webelement) using the text.
        :param element: Webelement that references the static dropdown.
        :param text: The text value to be selected.
        :return: None
        """
        dropdown = Select(element)
        dropdown.select_by_visible_text(text)

    def select_value_from_dropdown_index(self, element, index: int):
        """
        Selects the value from the passed list (webelement) using the index value.
        :param element: Webelement that references the static dropdown.
        :param index: The index value to be selected.
        :return: None
        """
        dropdown = Select(element)
        dropdown.select_by_index(index)

    def get_logger(self, file_name: str = "logfile.log", level: str = "INFO") -> object:
        """
        Creates the logger object and defines the logging level.
        :param file_name: The file name of the log. The default value is logfile.log.
        :param level:  The logging level. The default value is INFO.
        :return: logger object
        """
        # Fixing the name of the file in the logs (otherwise it will be the name of the baseclass)
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)
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

    def get_faker(self, locale: str = "pl_PL"):
        """
        Creates the faker object with given locale and returns it.
        :param locale: Lets you define the locale of the fake data. Default value is pl_Pl.
        :return: faker object
        """
        return MyFaker(locale)
