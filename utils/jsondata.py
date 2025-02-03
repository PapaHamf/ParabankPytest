import json
import datetime
import os

from datetime import datetime, timedelta
from utils.testdataset import TestDataSet
from logging import Logger


class JSONData(TestDataSet):

    def __init__(self, test_scenario: str, testcase: str, log: Logger):
        super().__init__(test_scenario, testcase)
        self._log: Logger = log

    @staticmethod
    def get_json_data(file_name: str) -> list [dict] | bool:
        """
        Returns the data from the JSON file as a dictionary.
        :param file_name: Filename of the JSON file.
        :return: List of dictionaries w/ data or false is file is not found.
        """
        log: Logger = log
        try:
            with open(file_name) as file_handle:
                json_data: dict = json.load(file_handle)
        except FileNotFoundError:
            log.warning(f"File {file_name} not found.")
        return json_data if len(json_data) > 0 else False

    @staticmethod
    def save_json_data(file_name: str, data: list [dict]) -> None | bool:
        """
        Lets you save the formatted data to the Excel file. The first row
        will contain the column names used for the dictionary keys.
        :param file_name: Filename of the Excel file
        :param data: List of lists containing the data to be written. First list should
        should contain the table headers.
        :return: None or False if file already exists
        """
        log: Logger = log
        try:
            with open(file_name, "w") as file_handle:
                json.dump(data, file_handle, indent = 5)
        except FileExistsError:
            log.warning(f"File {file_name} already exists. Could not open the file for writing.")
            return False

    def save_data(self) -> None | bool:
        """
        Saves the data to the JSON file.
        The file name is created based on the date & the test scenario name.
        :return: None or False if there was an error saving the file.
        """
        # Adding the test case name
        self._data["testcase"] = self._testcase
        # Checking if the file exists
        files = os.listdir("../")
        valid_files = [file for file in files if self._test_scenario in file and date in file]
        date = datetime.now().date()
        time = datetime.now().time().strftime("%H:%M:%S")
        if len(valid_files) == 1:

            if not os.path.exists("../history"):
                os.mkdir("../history")
        # Saving the file
        file_name = f"{self._test_scenario}_{date}_{time}.json"
        try:
            with open(file_name, "w") as file_handle:
                json.dump(self._data, file_handle, indent = 5)
        except FileExistsError:
            self._log.warning("File already exists. Could not open the file for writing.")
