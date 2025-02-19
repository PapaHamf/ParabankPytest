class OperationError(Exception):
    """
    Common exception class.
    """

    def __init__(self, msg: str, element: dict = None):
        self.msg: str = msg
        self.element: dict = element

    def get_element(self) -> dict:
        """Returns the data that caused the exception"""
        return self.element

    def get_msg(self) -> str:
        """Returns the error message."""
        return self.msg