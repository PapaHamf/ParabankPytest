class TestDataSet():

    def __init__(self, test_scenario: str, testcase: str):
        """
        Class that is responsible for collecting the data used in test cases.
        It provides the methods to set and get the data.
        :param test_scenario: Name of the test scenario.
        :param testcase: Name of the test case.
        """
        self._data: dict = {}
        self._test_scenario: str = test_scenario
        self._testcase: str = testcase
        self._data[self._test_scenario] = self._test_scenario
        self._data[self._testcase] = {}

    def add_data(self, key: str, value: str) -> None:
        """
        Allows you to add the test case data to the dictionary.
        :param key: The key of the dictionary entry.
        :param value: The value of the dictionary entry.
        :return:
        """
        self._data[self._testcase][key] = value

    def remove_data_by_key(self, key: str) -> None:
        """
        Allows you to remove the test case data from the dictionary by key.
        :param key: The key of the dictionary entry.
        :return:
        """
        self._data[self._testcase].pop(key)

    def remove_data_by_value(self, value: str) -> None:
        """
        Allows you to remove the test case data from the dictionary by value.
        :param value: The value of the dictionary entry.
        :return:
        """
        self._data[self._testcase] = { key:val for key, val in self._data[self._testcase].items() if val != value }

    def get_data(self) -> dict:
        """
        Returns the dictionary with data from the current test case.
        :return:
        """
        return self._data[self._testcase]

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
