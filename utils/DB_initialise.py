import openpyxl
from jaydebeapi import DatabaseError
from logging import Logger

from utils.exceldata import ExcelData
from utils.hysqlconnector import HyperSQLConnector

class DataBaseInitialise():
    """
    Class used for initializing the database before running tests.
    """

    # Declaring the table names
    DB_ACCOUNT = "account"
    DB_CUSTOMER = "customer"
    DB_POSITION = "positions"
    DB_STOCK = "stock"
    DB_TRANSACTION = "transaction"

    def __init__(self):
        self._log = self.get_logger()
        self._db = HyperSQLConnector()
        self._db.get_cursor()

    def get_logger(self, file_name: str = "logfile.log", level: str = "INFO") -> Logger:
        """
        Creates the logger object and defines the logging level.
        :param file_name: The file name of the log. The default value is logfile.log.
        :param level:  The logging level. The default value is INFO.
        :return: logger object
        """
        # Fixing the name of the file in the logs (otherwise it will be the name of the baseclass)
        logger_name = inspect.stack()[1][3]
        logger: Logger = logging.getLogger(logger_name)
        # Check if the logger already exits to avoid creating new logger in parametrized tests.
        if not len(logger.handlers):
            # Defining the log file
            file_handler = logging.FileHandler(file_name)
            # Defining the log format
            file_formater = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
            file_handler.setFormatter(file_formater)
            logger.addHandler(file_handler)
            # Setting the minimum level
            logger.setLevel(level)
        return logger

    def clean_database(self) -> None:
        """
        Initializes the dabatase by truncating the existing tables: TRANSACTION, ACCOUNT, POSITION,
        CUSTOMER and STOCK.
        :return:
        """
        self._log.info("Cleaning the database.")
        try:
            self._log.info("Purging the Transaction table.")
            self._db.execute_sql_statement(f"TRUNCATE TABLE {DataBaseInitialise.DB_TRANSACTION}")
        except DatabaseError:
            self._log.warning(f"Could not find the {DataBaseInitialise.DB_TRANSACTION} database table.")
            raise
        try:
            self._log.info("Purging the Account table.")
            self._db.execute_sql_statement(f"TRUNCATE TABLE {DataBaseInitialise.DB_ACCOUNT}")
        except DatabaseError:
            self._log.warning(f"Could not find the {DataBaseInitialise.DB_ACCOUNT} database table.")
            raise
        try:
            self._log.info("Purging the Position table.")
            self._db.execute_sql_statement(f"TRUNCATE TABLE {DataBaseInitialise.DB_POSITION}")
        except DatabaseError:
            self._log.warning(f"Could not find the {DataBaseInitialise.DB_POSITION} database table.")
            raise
        try:
            self._log.info("Purging the Customer table.")
            self._db.execute_sql_statement(f"TRUNCATE TABLE {DataBaseInitialise.DB_CUSTOMER}")
        except DatabaseError:
            self._log.warning(f"Could not find the {DataBaseInitialise.DB_CUSTOMER} database table.")
            raise
        try:
            self._log.info("Purging the Stock table.")
            self._db.execute_sql_statement(f"TRUNCATE TABLE {DataBaseInitialise.DB_STOCK}")
        except DatabaseError:
            self._log.warning(f"Could not find the {DataBaseInitialise.DB_STOCK} database table.")
            raise

    def populate_database(self):
        """
        Inserts the data from the Excel files into respective database tables.
        The tables are populated in the following sequence: Customer, Account, Transaction.
        This is due to foreign key restrictions.
        :return:
        """
        pass

    def get_database_table_customer(self):
        """
        Returns the Customer table from the database.
        :return:
        """
        return self._db.get_data_from_db(f"SELECT * FROM {DataBaseInitialise.DB_CUSTOMER}")

    def get_database_table_account(self):
        """
        Returns the Account table from the database.
        :return:
        """
        return self._db.get_data_from_db(f"SELECT * FROM {DataBaseInitialise.DB_ACCOUNT}")

    def get_database_table_transaction(self):
        """
        Returns the Transaction table from the database.
        :return:
        """
        return self._db.get_data_from_db(f"SELECT * FROM {DataBaseInitialise.DB_TRANSACTION}")

    def get_database_table_stock(self):
        """
        Returns the Stock table from the database.
        :return:
        """
        return self._db.get_data_from_db(f"SELECT * FROM {DataBaseInitialise.DB_STOCK}")


DBini = DataBaseInitialise()
DBini.clean_database()
print(DBini.get_database_table_account())