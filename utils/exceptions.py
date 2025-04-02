class OperationError(Exception):
    """
    Common exception class.
    :param msg: Message of the error.
    :param testcase: The name of the test case that caused the exception.
    :param user_data: User data used in the test case.
    """

    def __init__(self, msg: str, testcase: str = None, user_data: dict = None):
        self._msg: str = msg
        self._testcase: str = testcase
        self._user_data: dict = user_data

    def get_testcase(self) -> str:
        """
        Returns the test case name that caused the exception.
        :return: Test case name
        """
        return self._testcase

    def get_msg(self) -> str:
        """
        Returns the error message.
        :return: Error message
        """
        return self._msg

    def get_userdata(self) -> dict:
        """
        Returns the user data.
        :return: Dict containing the user data.
        """
        return self._user_data

class WebElementError(OperationError):
    """
    Webelement exception class.
    :param msg: Message of the error.
    :param failed_webelement: Webelement that caused the exception.
    :param testcase: The name of the test case that caused the exception.
    :param user_data: User data used in the test case.
    """

    def __init__(self, msg: str, failed_webelement: str, testcase: str = None, user_data: dict = None):
        super().__init__(msg, testcase, user_data)
        self._failed_webelement = failed_webelement