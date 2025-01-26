import jaydebeapi

class HyperSQLConnector():

    def __init__(self):
        """
        Class that allows you to connect to HyperSQL database server.
        """
        self._server = "localhost"
        self._driver = "org.hsqldb.jdbcDriver"
        self._URL = f"jdbc:hsqldb:hsql://{self._server}/Parabank"
        self._database = "/"
        self._username = "SA"
        self._password = ""
        self._credentials =[self._username, self._password]
        self._path_to_driver = "/opt/drivers/hsqldb.jar"

    def get_cursor(self):
        """
        Returns the jaydebeapi cursor to the database.
        :return:
        """
        connection = jaydebeapi.connect(self._driver, self._URL, self._credentials, self._path_to_driver)
        try:
            connection.autocommit = 0
            cursor = connection.cursor()
            return cursor
        except Exception as error:
            connection.rollback()
            raise error

data = HyperSQLConnector()
cursor = data.get_cursor()
select = "SELECT * FROM Transaction"
cursor.execute(select)
results = cursor.fetchall()
for row in results:
    print(row)
select_accounts = "SELECT * FROM Account"
cursor.execute(select_accounts)
results2 = cursor.fetchall()
for row in results2:
    print(row)