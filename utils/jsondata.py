import json
import datetime
import os

from datetime import datetime

from utils.exceptions import OperationError
from utils.testdataset import TestDataSet
from logging import Logger


class JSONData(TestDataSet):
    """
    Class that provides the methods to handle the test data in JSON files.
    :param test_scenario: The name of the test scenario.
    :param testcase: The name of the current test case.
    :param log: Logger object.
    """

    DIR_PREFIX: str = "../testdata/"

    def __init__(self, test_scenario: str, testcase: str, log: Logger):
        super().__init__(test_scenario, testcase)
        self._log: Logger = log

    def convert_time_to_seconds(self, time: str) -> int:
        """
        Converts the given time string to the number of seconds.
        :param time: The time in the hh:mm:ss format.
        :return:
        """
        return sum(x * int(t) for x, t in zip([3600, 60, 1], time.split(":")))

    @staticmethod
    def get_json_data(file_name: str, log: Logger) -> dict:
        """
        Returns the data from the JSON file as a dictionary.
        :param file_name: Filename of the JSON file.
        :param log: Logger object
        :return: Dictionary w/ data.
        """
        log: Logger = log
        try:
            with open(JSONData.DIR_PREFIX + file_name) as file_handle:
                json_data: dict = json.load(file_handle)
        except FileNotFoundError as error:
            log.warning(f"File {JSONData.DIR_PREFIX + file_name} not found.")
            raise OperationError(error.strerror)
        return json_data

    @staticmethod
    def save_json_data(file_name: str, data: dict, log: Logger) -> None:
        """
        Lets you save the formatted data to the JSON file.
        :param file_name: Filename of the JSON file
        :param data: Dictionary containing the data to be written.
        :param log: Logger object
        :return: None
        """
        log: Logger = log
        try:
            with open(self.DIR_PREFIX + file_name, "w") as file_handle:
                json.dump(data, file_handle, indent = 5)
        except IOError as error:
            log.warning(f"Could not open the file {JSONData.DIR_PREFIX + file_name} for writing.")
            raise OperationError(error.strerror)


    def save_data(self, timediff: int = 60) -> None:
        """
        Saves the data to the JSON file.
        The file name is created based on the date & the test scenario name.
        :param timediff: Time difference used to add testcases to the same test scenario file. Default value is 60.
        :return: None.
        """
        # Checking if the file exists
        date = datetime.now().date()
        time = datetime.now().time().strftime("%H:%M:%S")
        # Fetching the list of the existing files
        files = os.listdir(self.DIR_PREFIX)
        valid_files = [file for file in files if self._test_scenario in file and str(date) in file]
        if len(valid_files) == 1:
            # Create the directory /history to archive the previous scenarios
            if not os.path.exists(self.DIR_PREFIX + "history"):
                os.mkdir(self.DIR_PREFIX + "history")
            # Extracting the time from the name of the existing file
            file_time = valid_files[0].split("_")[2]
            if self.convert_time_to_seconds(time) - self.convert_time_to_seconds(file_time.split(".")[0]) > timediff:
                os.replace(self.DIR_PREFIX + valid_files[0], self.DIR_PREFIX + "history/" + valid_files[0])
                file_name = f"{self._test_scenario}_{date}_{time}.json"
            else:
                file_name = valid_files[0]
                self._data.update(JSONData.get_json_data(file_name, self._log))
        else:
            file_name = f"{self._test_scenario}_{date}_{time}.json"
        # Saving the file
        try:
            with open(self.DIR_PREFIX + file_name, "w") as file_handle:
                json.dump(self._data, file_handle, indent = 5)
        except IOError as error:
            self._log.warning(f"Could not open the file {self.DIR_PREFIX + file_name} for writing.")
            raise OperationError(error.strerror, self._testcase)
