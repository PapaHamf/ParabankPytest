import openpyxl
import logging
import inspect
from jaydebeapi import DatabaseError
from logging import Logger

from utils.exceldata import ExcelData
from utils.hysqlconnector import HyperSQLConnector
from utils.exceptions import OperationError

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
        Initializes the database by truncating the existing tables: TRANSACTION, ACCOUNT, POSITION,
        CUSTOMER and STOCK.
        :return:
        """
        self._log.info("Cleaning the database.")
        try:
            self._log.info("Purging the Transaction table.")
            self._db.execute_sql_statement(f"TRUNCATE TABLE {DataBaseInitialise.DB_TRANSACTION}")
        except DatabaseError as error:
            self._log.warning(f"Could not find the {DataBaseInitialise.DB_TRANSACTION} database table.")
            raise OperationError(error.__str__())
        try:
            self._log.info("Purging the Account table.")
            self._db.execute_sql_statement(f"TRUNCATE TABLE {DataBaseInitialise.DB_ACCOUNT}")
        except DatabaseError as error:
            self._log.warning(f"Could not find the {DataBaseInitialise.DB_ACCOUNT} database table.")
            raise OperationError(error.__str__())
        try:
            self._log.info("Purging the Position table.")
            self._db.execute_sql_statement(f"TRUNCATE TABLE {DataBaseInitialise.DB_POSITION}")
        except DatabaseError as error:
            self._log.warning(f"Could not find the {DataBaseInitialise.DB_POSITION} database table.")
            raise OperationError(error.__str__())
        try:
            self._log.info("Purging the Customer table.")
            self._db.execute_sql_statement(f"TRUNCATE TABLE {DataBaseInitialise.DB_CUSTOMER}")
        except DatabaseError as error:
            self._log.warning(f"Could not find the {DataBaseInitialise.DB_CUSTOMER} database table.")
            raise OperationError(error.__str__())
        try:
            self._log.info("Purging the Stock table.")
            self._db.execute_sql_statement(f"TRUNCATE TABLE {DataBaseInitialise.DB_STOCK}")
        except DatabaseError as error:
            self._log.warning(f"Could not find the {DataBaseInitialise.DB_STOCK} database table.")
            raise OperationError(error.__str__())

    def populate_database(self):
        """
        Inserts the data from the Excel files into respective database tables.
        The tables are populated in the following sequence: Customer, Account, Transaction.
        This is due to foreign key restrictions.
        :return:
        """
        customer_data = ExcelData.get_excel_data(ExcelData.DIR_PREFIX + ExcelData.DATASET_CUSTOMER, self._log)
        # Inserting the customer data (w/ usernames & passwords)
        try:
            for customer in customer_data:
                values = ", ".join(str(int(value)) if isinstance(value, float) else f"'{value}'" for value in customer.values())
                self._db.execute_sql_statement(f"INSERT INTO {DataBaseInitialise.DB_CUSTOMER} VALUES ({values})")
        except DatabaseError as error:
            self._log.warning(f"Error while inserting data into {DataBaseInitialise.DB_CUSTOMER} table.")
            self._log.warning(f"Data: {values}")
            raise OperationError(error.__str__())
        account_data = ExcelData.get_excel_data(ExcelData.DIR_PREFIX + ExcelData.DATASET_ACCOUNT, self._log)
        # Inserting the account data
        try:
            for account in account_data:
                values = ", ".join(str(int(value)) if isinstance(value, float) else f"'{value}'" for value in account.values())
                self._db.execute_sql_statement(f"INSERT INTO {DataBaseInitialise.DB_ACCOUNT} VALUES ({values})")
        except DatabaseError as error:
            self._log.warning(f"Error while inserting data into {DataBaseInitialise.DB_ACCOUNT} table.")
            self._log.warning(f"Data: {values}")
            raise OperationError(error.__str__())
        transaction_data = ExcelData.get_excel_data(ExcelData.DIR_PREFIX + ExcelData.DATASET_TRANSACTION, self._log)
        # Inserting the transaction data
        try:
            for transaction in transaction_data:
                values = ", ".join(str(int(value)) if isinstance(value, float) else f"'{value}'" for value in transaction.values())
                self._db.execute_sql_statement(f"INSERT INTO {DataBaseInitialise.DB_TRANSACTION} VALUES ({values})")
        except DatabaseError as error:
            self._log.warning(f"Error while inserting data into {DataBaseInitialise.DB_TRANSACTION} table.")
            self._log.warning(f"Data: {values}")
            raise OperationError(error.__str__())

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
DBini.populate_database()