import logging
import inspect
import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

@pytest.mark.usefixtures("setup")
class BaseClass:

    def verify_element_presence(self, locator: str, timeout: int = 10) -> None:
        """
            Verifies the web element presence on the page.
            Accepts two arguments. First one is the locator (using the By.XPATH),
            and the second one is a timeout: int.
            :return: None
        """
        wait = WebDriverWait(self._driver, timeout)
        wait.until(expected_conditions.presence_of_element_located((By.XPATH, locator)))

    def get_logger(self, file_name: str = "logfile.log", level: str = "INFO") -> object:
        """
            Creates the logger object and defines the logging level.
            Accepts two arguments. First one is the file name of the log,
            and the second one is the logging level.
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