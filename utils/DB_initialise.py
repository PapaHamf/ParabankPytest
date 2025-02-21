import logging
import inspect

from utils.exceldata import ExcelData
from utils.hysqlconnector import HyperSQLConnector
from utils.exceptions import OperationError
from jaydebeapi import DatabaseError
from logging import Logger


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

    def truncate_table(self, table_name: str) -> None:
        """
        Truncates the given table of the database.
        :param table_name: The name of the table to truncate/delete from.
        :return:
        """
        try:
            self._log.info(f"Purging the {table_name.capitalize()} table.")
            self._db.execute_sql_statement(f"TRUNCATE TABLE {table_name}")
        except DatabaseError as error:
            self._log.warning(f"Could not find the {table_name.capitalize()} database table.")
            raise OperationError(error.__str__())

    def insert_table(self, table_name: str, dataset: str) -> None:
        """
        Inserts the given data set to the table of the database.
        :param table_name: The name of the table to insert data to.
        :param dataset: Data set that will be inserted into DB.
        :return:
        """
        read_data = ExcelData.get_excel_data(ExcelData.DIR_PREFIX + dataset, log = self._log)
        try:
            self._log.info(f"Inserting the data into {table_name.capitalize()} table.")
            for single_data in read_data:
                values = ", ".join(str(int(value)) if isinstance(value, float) else f"'{value}'" for value in single_data.values())
                self._db.execute_sql_statement(f"INSERT INTO {table_name} VALUES ({values})")
            self._log.info("Inserting completed successfully.")
        except DatabaseError as error:
            self._log.warning(f"Error while inserting data into {table_name.capitalize()} table.")
            self._log.warning(f"Data: {values}")
            raise OperationError(error.__str__())

    def purge_database(self) -> None:
        """
        Initializes the database by truncating the existing tables: TRANSACTION, ACCOUNT, POSITION,
        CUSTOMER and STOCK.
        :return:
        """
        self._log.info("Cleaning the database.")
        self.truncate_table(DataBaseInitialise.DB_TRANSACTION)
        self.truncate_table(DataBaseInitialise.DB_ACCOUNT)
        self.truncate_table(DataBaseInitialise.DB_POSITION)
        self.truncate_table(DataBaseInitialise.DB_CUSTOMER)
        self.truncate_table(DataBaseInitialise.DB_STOCK)

    def populate_database(self):
        """
        Inserts the data from the Excel files into respective database tables.
        The tables are populated in the following sequence: Customer, Account, Transaction.
        This is due to foreign key restrictions.
        :return:
        """
        # Inserting the customer data (w/ usernames & passwords)
        self.insert_table(DataBaseInitialise.DB_CUSTOMER, ExcelData.DATASET_CUSTOMER)
        # Inserting the account data
        self.insert_table(DataBaseInitialise.DB_ACCOUNT, ExcelData.DATASET_ACCOUNT)
        # Inserting the transaction data
        self.insert_table(DataBaseInitialise.DB_TRANSACTION, ExcelData.DATASET_TRANSACTION)

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

if __name__ == "__main__":
    DBini = DataBaseInitialise()
    # DBini.purge_database()
    # DBini.populate_database()
    print(DBini.get_database_table_transaction())