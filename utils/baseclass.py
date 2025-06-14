import pytest
import logging
import inspect

from logging import Logger
from utils.myfaker import MyFaker

@pytest.mark.usefixtures("setup")
class BaseClass():
    """
    Base class for all the test scenarios.
    """

    DIR_PREFIX: str = "./testdata/"

    def get_logger(self, file_name: str = "logfile.log", level: str = "INFO") -> Logger:
        """
        Creates the logger object and defines the logging level.
        :param file_name: The file name of the log. The default value is logfile.log.
        :param level:  The logging level. The default value is INFO.
        :return: logger object
        """
        # Fixing the name of the file in the logs (otherwise it will be the name of the baseclass)
        self._logger_name = inspect.stack()[1][3]
        self._logger: Logger = logging.getLogger(self._logger_name)
        # Check if the logger already exits to avoid creating new logger in parametrized tests.
        if not len(self._logger.handlers):
            # Defining the log file
            self._file_handler = logging.FileHandler(self.DIR_PREFIX + file_name)
            # Defining the log format
            self._file_formater = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
            self._file_handler.setFormatter(self._file_formater)
            self._logger.addHandler(self._file_handler)
            # Setting the minimum level
            self._logger.setLevel(level)
        return self._logger

    def get_faker(self, locale: str = "pl_PL") -> MyFaker:
        """
        Creates the faker object with specified locale and returns it.
        :param locale: Lets you define the locale of the fake data. Default value is pl_Pl.
        :return: faker object
        """
        return MyFaker(locale)