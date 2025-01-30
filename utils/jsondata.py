import datetime
import os
from datetime import datetime

import json

class JSONData():

    def __init__(self, test_scenario: str, testcase: str, log):
        self._data: dict = {}
        self._test_scenario = test_scenario
        self._testcase: str = testcase
        self._log = log

    def add_data(self, key: str, value: str) -> None:
        """
        Allows you to add the test case data to the dictionary.
        :param key: The key of the dictionary entry.
        :param value: The value of the dictionary entry.
        :return:
        """
        self._data[key] = value

    def remove_data_by_key(self, key: str) -> None:
        """
        Allows you to remove the test case data from the dictionary by key.
        :param key: The key of the dictionary entry.
        :return:
        """
        self._data.pop(key)

    def remove_data_by_value(self, value: str) -> None:
        """
        Allows you to remove the test case data from the dictionary by value.
        :param value: The value of the dictionary entry.
        :return:
        """
        self._data = { key:val for key, val in self._data.items() if val != value }

    def get_data(self) -> dict:
        """
        Returns the dictionary with data from the current test case.
        :return:
        """
        return self._data

    def get_testcase(self) -> str:
        """
        Returns the current test case name.
        :return:
        """
        return self._testcase

    def get_test_scenario(self) -> str:
        """
        Returns the current test scenario name.
        :return:
        """
        return self._test_scenario

    def save_data(self) -> None:
        """
        Saves the data to the JSON file.
        The file name is created based on the date & the test scenario name.
        :return:
        """
        # Adding the test case name
        self._data["testcase"] = self._testcase
        # Checking if the file exists
        files = os.listdir("../")
        valid_files = [file for file in files if self._test_scenario in file and date in file]
        date = datetime.now().date()
        time = datetime.now().time().strftime("%H:%M:%S")
        if len(valid_files) == 1:

        # Saving the file
        file_name = f"{self._test_scenario}_{date}_{time}.json"
        try:
            with open(file_name, "w") as file_handle:
                json.dump(self._data, file_handle, indent = 5)
        except FileExistsError:
            self._log.warn("File already exists. Could not open the file for writing.")


    def read_data(self, testcase: str, date: str) -> dict | list [dict]:
        """
        Reads the data from the JSON file or mutiple files if there are multiple test cases
        with the same name & date.
        :param testcase: The name of the testcase for which the data should be read.
        :param date: The date when the testcase was ran.
        :return:
        """
        files = os.listdir("../")
        valid_files = [file for file in files if testcase in file and date in file]
        if len(valid_files) == 1:
            # Reading the data
            try:
                with open(valid_files[0]) as file_handle:
                    excel_data: dict = json.load(file_handle)
            except FileNotFoundError:
                self._log.warn("File not found.")
        elif len(valid_files) > 1:
            for file in valid_files:
                # Declaring temporary list
                excel_data: list = []
                # Reading the data
                with open(file) as file_handle:
                    temp_dict = json.load(file_handle)
                excel_data.append(temp_dict)
        else:
            excel_data = None
        return excel_data