import jaydebeapi

from utils.exceptions import OperationError

class HyperSQLConnector():
    """
    Class that allows you to connect to HyperSQL database server.
    """

    def __init__(self):
        self._server: str = "localhost"
        self._driver: str = "org.hsqldb.jdbcDriver"
        self._URL: str = f"jdbc:hsqldb:hsql://{self._server}/parabank"
        self._username: str = "SA"
        self._password: str = ""
        self._credentials: list = [self._username, self._password]
        self._path_to_driver: str = "./utils/hsqldb.jar"

    def get_cursor(self) -> None:
        """
        Creates the jaydebeapi cursor to the database.
        :return: None
        """
        self._connection = jaydebeapi.connect(self._driver, self._URL, self._credentials, self._path_to_driver)
        try:
            self._connection.autocommit = 0
            self._cursor = self._connection.cursor()
        except Exception as error:
            self._connection.rollback()
            raise OperationError(error.__str__())

    def get_data_from_db(self, statement: str) -> list:
        """
        Returns the results of the database query in the SQL statement.
        :param statement: SQL statement that will be executed in the DB.
        :return: List w/ data
        """
        self._cursor.execute(statement)
        return self._cursor.fetchall()

    def execute_sql_statement(self, statement: str) -> None:
        """
        Lets you insert the data into the database or create and drop tables.
        :param statement: SQL statement that will be executed in the DB.
        :return:
        """
        self._cursor.execute(statement)
        self._connection.commit()

    def close_connection(self) -> None:
        """
        Closes the connection w/ the database.
        :return:
        """
        self._connection.close()
