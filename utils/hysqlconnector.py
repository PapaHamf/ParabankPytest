import jaydebeapi

class HyperSQLConnector():

    def __init__(self):
        """
        Class that allows you to connect to HyperSQL database server.
        """
        self._server: str = "localhost"
        self._driver: str = "org.hsqldb.jdbcDriver"
        self._URL: str = f"jdbc:hsqldb:hsql://{self._server}/Parabank"
        self._username: str = "SA"
        self._password: str = ""
        self._credentials: list = [self._username, self._password]
        self._path_to_driver: str = "/opt/drivers/hsqldb.jar"

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
            raise error

    def get_data_from_db(self, statement: str) -> list:
        """
        Returns the results of the database query passed in the SQL statement.
        :param statement: SQL statement that will be executed in the DB.
        :return: list
        """
        self._cursor.execute(statement)
        return self._cursor.fetchall()

    def execute_sql_statement(self, statement: str) -> None:
        """
        Lets you insert the data into the database or create and drop tables.
        :param statement: SQL statement that will be executed in the DB.
        :return: None
        """
        self._cursor.execute(statement)
        self._connection.commit()

    def close_connection(self) -> None:
        """
        Closes the connection w/ the database.
        :return: None
        """
        self._connection.close()
