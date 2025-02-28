import csv

from utils.testdataset import TestDataSet
from utils.exceptions import OperationError
from utils.baseclass import BaseClass
from logging import Logger

class CSVData(TestDataSet):
    """
    Class that provides the methods to handle the test data in CSV format.
    :param test_scenario: The name of the test scenario.
    :param testcase: The name of the current test case.
    """

    DIR_PREFIX: str = "../testdata/"

    def __init__(self, test_scenario: str, testcase: str):
        super().__init__(test_scenario, testcase)
        self._baseclass: BaseClass = BaseClass()
        self._log: Logger = self._baseclass.get_logger()

    @staticmethod
    def get_csv_data(file_name: str):
        """
        Returns the data from the CSV file as a dictionary.
        The first row should contain the column names used for the dictionary keys.
        :param file_name: Filename of the CSV file.
        :return: List of dictionaries w/ data.
        """
        baseclass: BaseClass = BaseClass()
        log = baseclass.get_logger()
        try:
            csv_data: list = []
            with open(CSVData.DIR_PREFIX + file_name, "r", encoding = "utf-8-sig") as file_handle:
                reader = csv.DictReader(file_handle)
                for row in reader:
                    csv_data.append(row)
        except FileNotFoundError as error:
            log.warning(f"File {CSVData.DIR_PREFIX + file_name} not found.")
            raise OperationError(error.strerror)
        return csv_data
