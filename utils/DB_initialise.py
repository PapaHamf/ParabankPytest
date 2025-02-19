import openpyxl
from jaydebeapi import DatabaseError

from utils.exceldata import ExcelData
from utils.baseclass import BaseClass
from utils.hysqlconnector import HyperSQLConnector

class DataBaseInitialise(BaseClass):

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