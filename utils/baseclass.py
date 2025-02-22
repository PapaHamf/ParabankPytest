import logging
import inspect

from faker import Faker
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

class BaseClass():
    """
    Base class for all the test scenarios.
    """

    DIR_PREFIX: str = "../testdata/"

    def __init__(self):
        self._log: Logger = self.get_logger()
        self._faker: MyFaker = self.get_faker()

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
            file_handler = logging.FileHandler(self.DIR_PREFIX + file_name)
            # Defining the log format
            file_formater = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
            file_handler.setFormatter(file_formater)
            logger.addHandler(file_handler)
            # Setting the minimum level
            logger.setLevel(level)
        return logger

    def get_faker(self, locale: str = "pl_PL") -> MyFaker:
        """
        Creates the faker object with given locale and returns it.
        :param locale: Lets you define the locale of the fake data. Default value is pl_Pl.
        :return: faker object
        """
        return MyFaker(locale)