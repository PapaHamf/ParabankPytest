import pytest
import allure
import random

from utils.baseclass import BaseClass
from utils.exceldata import ExcelData
from utils.hysqlconnector import HyperSQLConnector
from pageobjects.homepage import HomePage
from pageobjects.basepage import BasePage

class TestOpenAccount(BaseClass):

    @allure.title("Logging in/out the user")
    @pytest.fixture(scope = "function")
    def login_logout(self):
        """
        Logins the user in the app and logs him out after the test.
        :return: List containing the dict w/ the home page object and user data.
        """
        with allure.step("Step 1: Logging in"):
            log = self.get_logger()
            self.driver.get(BasePage.HOME_PAGE)
            # Get the user data from Excel file
            user_data = random.choice(ExcelData.get_excel_data("dataset_customer.xlsx"))
            user_name = user_data["username"]
            password = user_data["password"]
            log.info("Logging the user.")
            # Create the home page object
            home_page = HomePage(self.driver)
            log.info(f"User name: {user_name}")
            home_page.get_username().send_keys(user_name)
            log.info(f"Password: {password}")
            home_page.get_password().send_keys(password)
            log.info("Clicking the login button.")
            side_menu = home_page.get_login_button()
        yield side_menu, user_data
        # Log out the user
        with allure.step("Step 2: Logging out"):
            log.info(f"Logging out the user {user_name}.")
            side_menu.get_log_out_link().click()
            self.driver.delete_all_cookies()

    @allure.parent_suite("Tests for Parabank application")
    @allure.suite("Tests for funds transfer")
    @allure.sub_suite("Positive funds transfer tests")
    @allure.tag("Funds transfer", "New transfer", "Positive")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.label("owner", "Parasoft")
    @allure.testcase("Test case no 80")
    @allure.description("This test attempts to transfer funds from one account to other.")
    @pytest.mark.smoke
    @pytest.mark.usefixtures("login_logout")
    @pytest.mark.skip
    def test_transfer_funds_postive(self, login_logout):
        """
        Tests the funds transfer between accounts.
        :return:
        """
        log = self.get_logger()
        log.info("Clicking the Transfer Funds link.")
        transfer_funds = login_logout[0].get_transfer_funds_page()
        data_collection = ExcelData("Funds transfer", "New transfer")
        amount = str(random.randint(0, 10000))
        data_collection.add_data("amount", amount)
        log.info(f"Entering the transfer amount {amount}.")
        transfer_funds.get_amount().send_keys(amount)
        source_accounts_list = transfer_funds.get_list_values(transfer_funds.get_source_accounts())
        src_acc_no = random.choice(source_accounts_list)
        data_collection.add_data("source_account", src_acc_no)
        log.info(f"Selecting the source account {src_acc_no}")
        transfer_funds.select_value_from_dropdown_text(transfer_funds.get_source_accounts(), src_acc_no)
        target_accounts_list = transfer_funds.get_list_values(transfer_funds.get_target_accounts())
        trg_acc_no = random.choice(target_accounts_list)
        data_collection.add_data("target_account", trg_acc_no)
        log.info(f"Selecting the target account {trg_acc_no}")
        transfer_funds.select_value_from_dropdown_text(transfer_funds.get_target_accounts(), trg_acc_no)
        log.info("Clicking the Transfer button.")
        transfer_funds.get_transfer_button().click()
        assert transfer_funds.get_transfer_complete().text == transfer_funds.TRANSFER_SUCCESS_MSG

    @allure.parent_suite("Tests for Parabank application")
    @allure.suite("Tests for funds transfer")
    @allure.sub_suite("Positive funds transfer tests")
    @allure.tag("Funds transfer", "New transfer", "Target list")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.label("owner", "Parasoft")
    @allure.testcase("Test case no 81")
    @allure.description("This test verifies if the selected source account is removed from the target account list.")
    @pytest.mark.smoke
    @pytest.mark.usefixtures("login_logout")
    @pytest.mark.skip
    def test_transfer_funds_removed_from_target(self, login_logout):
        """
        Tests if the source account is not on target account list.
        :return:
        """
        log = self.get_logger()
        log.info("Clicking the Transfer Funds link.")
        transfer_funds = login_logout[0].get_transfer_funds_page()
        data_collection = ExcelData("Funds transfer", "Removed target")
        amount = str(random.randint(0, 10000))
        data_collection.add_data("amount", amount)
        log.info(f"Entering the transfer amount {amount}.")
        transfer_funds.get_amount().send_keys(amount)
        source_accounts_list = transfer_funds.get_list_values(transfer_funds.get_source_accounts())
        src_acc_no = random.choice(source_accounts_list)
        data_collection.add_data("source_account", src_acc_no)
        log.info(f"Selecting the source account {src_acc_no}")
        transfer_funds.select_value_from_dropdown_text(transfer_funds.get_source_accounts(), src_acc_no)
        target_accounts_list = transfer_funds.get_list_values(transfer_funds.get_target_accounts())
        # Remove the source account from the source_accounts_list
        source_accounts_list.remove(src_acc_no)
        assert target_accounts_list == source_accounts_list

    @allure.parent_suite("Tests for Parabank application")
    @allure.suite("Tests for funds transfer")
    @allure.sub_suite("Negative funds transfer tests")
    @allure.tag("Funds transfer", "New transfer", "Negative", "Insufficient funds")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.label("owner", "Parasoft")
    @allure.testcase("Test case no 82")
    @allure.description("This test attempts to transfer funds from the account with insufficient funds.")
    @pytest.mark.smoke
    @pytest.mark.usefixtures("login_logout")
    @pytest.mark.skip
    def test_transfer_funds_insufficient_funds(self, login_logout):
        """
        Tests the funds transfer with insufficient funds.
        :return:
        """
        log = self.get_logger()
        log.info("Clicking the Transfer Funds link.")
        transfer_funds = login_logout[0].get_transfer_funds_page()
        data_collection = ExcelData("Funds transfer", "Insufficient funds")
        # Choose the source account first
        source_accounts_list = transfer_funds.get_list_values(transfer_funds.get_source_accounts())
        src_acc_no = random.choice(source_accounts_list)
        # Fetch the account balance from the database
        db_handle = HyperSQLConnector()
        db_handle.get_cursor()
        db_data = db_handle.get_data_from_db(f"SELECT balance FROM account "
                                             f"WHERE id = '{src_acc_no}'")
        if len(db_data) > 0:
            acc_balance = db_data[0][0]
        else:
            acc_balance = 0
        # Increase the amount to exceed the balance
        amount = str(acc_balance + 5000)
        data_collection.add_data("amount", amount)
        log.info(f"Entering the transfer amount {amount}.")
        transfer_funds.get_amount().send_keys(amount)
        data_collection.add_data("source_account", src_acc_no)
        log.info(f"Selecting the source account {src_acc_no}")
        transfer_funds.select_value_from_dropdown_text(transfer_funds.get_source_accounts(), src_acc_no)
        target_accounts_list = transfer_funds.get_list_values(transfer_funds.get_target_accounts())
        trg_acc_no = random.choice(target_accounts_list)
        data_collection.add_data("target_account", trg_acc_no)
        log.info(f"Selecting the target account {trg_acc_no}")
        transfer_funds.select_value_from_dropdown_text(transfer_funds.get_target_accounts(), trg_acc_no)
        log.info("Clicking the Transfer button.")
        transfer_funds.get_transfer_button().click()
        assert transfer_funds.get_amount_errors().text == transfer_funds.AMOUNT_INVALID_ERROR_MSG

    @allure.parent_suite("Tests for Parabank application")
    @allure.suite("Tests for funds transfer")
    @allure.sub_suite("Negative funds transfer tests")
    @allure.tag("Funds transfer", "New transfer", "Negative", "Same account")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.label("owner", "Parasoft")
    @allure.testcase("Test case no 83")
    @allure.description("This test attempts to transfer funds between the same account.")
    @pytest.mark.smoke
    @pytest.mark.usefixtures("login_logout")
    @pytest.mark.skip
    def test_transfer_funds_same_account(self, login_logout):
        """
        Tests the funds transfer between the same account.
        :return:
        """
        log = self.get_logger()
        log.info("Clicking the Transfer Funds link.")
        transfer_funds = login_logout[0].get_transfer_funds_page()
        data_collection = ExcelData("Funds transfer", "Same account")
        amount = str(random.randint(0, 10000))
        data_collection.add_data("amount", amount)
        log.info(f"Entering the transfer amount {amount}.")
        transfer_funds.get_amount().send_keys(amount)
        source_accounts_list = transfer_funds.get_list_values(transfer_funds.get_source_accounts())
        src_acc_no = random.choice(source_accounts_list)
        data_collection.add_data("source_account", src_acc_no)
        log.info(f"Selecting the source account {src_acc_no}")
        transfer_funds.select_value_from_dropdown_text(transfer_funds.get_source_accounts(), src_acc_no)
        trg_acc_no = src_acc_no
        data_collection.add_data("target_account", trg_acc_no)
        log.info(f"Selecting the target account {trg_acc_no}")
        transfer_funds.select_value_from_dropdown_text(transfer_funds.get_target_accounts(), trg_acc_no)
        log.info("Clicking the Transfer button.")
        transfer_funds.get_transfer_button().click()
        assert transfer_funds.get_internal_error().text == transfer_funds.TRANSFER_ERROR_MSG

    @allure.parent_suite("Tests for Parabank application")
    @allure.suite("Tests for funds transfer")
    @allure.sub_suite("Positive funds transfer tests")
    @allure.tag("Funds transfer", "New transfer", "Verify accounts")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.label("owner", "Parasoft")
    @allure.testcase("Test case no 84")
    @allure.description("This test attempts to transfer funds from one account to other and verifies"
                        " if the source and target accounts are correct.")
    @pytest.mark.smoke
    @pytest.mark.usefixtures("login_logout")
    @pytest.mark.skip
    def test_transfer_funds_verify_accounts(self, login_logout):
        """
        Tests the funds transfer and verifies if the accounts are correct.
        :return:
        """
        log = self.get_logger()
        log.info("Clicking the Transfer Funds link.")
        transfer_funds = login_logout[0].get_transfer_funds_page()
        data_collection = ExcelData("Funds transfer", "Verify accounts")
        amount = str(random.randint(0, 10000))
        data_collection.add_data("amount", amount)
        log.info(f"Entering the transfer amount {amount}.")
        transfer_funds.get_amount().send_keys(amount)
        source_accounts_list = transfer_funds.get_list_values(transfer_funds.get_source_accounts())
        src_acc_no = random.choice(source_accounts_list)
        data_collection.add_data("source_account", src_acc_no)
        log.info(f"Selecting the source account {src_acc_no}")
        transfer_funds.select_value_from_dropdown_text(transfer_funds.get_source_accounts(), src_acc_no)
        target_accounts_list = transfer_funds.get_list_values(transfer_funds.get_target_accounts())
        trg_acc_no = random.choice(target_accounts_list)
        data_collection.add_data("target_account", trg_acc_no)
        log.info(f"Selecting the target account {trg_acc_no}")
        transfer_funds.select_value_from_dropdown_text(transfer_funds.get_target_accounts(), trg_acc_no)
        log.info("Clicking the Transfer button.")
        transfer_funds.get_transfer_button().click()
        with allure.step("Step 1: Verify if the transfer was successful"):
            assert transfer_funds.get_transfer_complete().text == transfer_funds.TRANSFER_SUCCESS_MSG
        with (allure.step("Step 2: Verify the account numbers")):
            assert transfer_funds.get_source_account_result().text == src_acc_no \
                    and transfer_funds.get_target_account_result().text == trg_acc_no

    @allure.parent_suite("Tests for Parabank application")
    @allure.suite("Tests for funds transfer")
    @allure.sub_suite("Positive funds transfer tests")
    @allure.tag("Funds transfer", "New transfer", "Verify transfer")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.label("owner", "Parasoft")
    @allure.testcase("Test case no 85")
    @allure.description("This test attempts to transfer funds from one account to other and verifies"
                        " if the funds were transferred correctly.")
    @pytest.mark.smoke
    @pytest.mark.usefixtures("login_logout")
    @pytest.mark.skip
    def test_transfer_funds_verify_transfer(self, login_logout):
        """
        Tests the funds transfer and verifies if the funds were transferred correctly.
        :return:
        """
        log = self.get_logger()
        log.info("Clicking the Transfer Funds link.")
        transfer_funds = login_logout[0].get_transfer_funds_page()
        data_collection = ExcelData("Funds transfer", "Verify transfer")
        amount = str(random.randint(0, 10000))
        data_collection.add_data("amount", amount)
        log.info(f"Entering the transfer amount {amount}.")
        transfer_funds.get_amount().send_keys(amount)
        source_accounts_list = transfer_funds.get_list_values(transfer_funds.get_source_accounts())
        src_acc_no = random.choice(source_accounts_list)
        data_collection.add_data("source_account", src_acc_no)
        log.info(f"Selecting the source account {src_acc_no}")
        transfer_funds.select_value_from_dropdown_text(transfer_funds.get_source_accounts(), src_acc_no)
        target_accounts_list = transfer_funds.get_list_values(transfer_funds.get_target_accounts())
        trg_acc_no = random.choice(target_accounts_list)
        data_collection.add_data("target_account", trg_acc_no)
        log.info(f"Selecting the target account {trg_acc_no}")
        transfer_funds.select_value_from_dropdown_text(transfer_funds.get_target_accounts(), trg_acc_no)
        log.info("Clicking the Transfer button.")
        transfer_funds.get_transfer_button().click()
        with allure.step("Step 1: Verify the debit on source account"):
            log.info("Clicking the Accounts Overview link.")
            accounts_overview = login_logout[0].get_accounts_overview_page()
            log.info("Clicking the source account link.")
            activity_page = accounts_overview.select_account_number(src_acc_no)
            log.info("Selecting the Debit from the Type list.")
            activity_page.select_value_from_dropdown_text(activity_page.get_activity_type(), "Debit")
            log.info("Clicking the Go button.")
            activity_page.get_activity_button().click()
            transaction = activity_page.get_transaction_by_index(-1)
            log.info(f"Verifying if the transaction name is {activity_page.FUNDS_SENT}")
            assert transaction[1] == activity_page.FUNDS_SENT
            log.info(f"Verifying if the transaction amount is {amount}.")
            assert str(transaction[2]).split(".")[0] == amount
        with allure.step("Step 2: Verify the credit on target account"):
            log.info("Clicking the Accounts Overview link.")
            accounts_overview = login_logout[0].get_accounts_overview_page()
            log.info("Clicking the target account link.")
            activity_page = accounts_overview.select_account_number(trg_acc_no)
            log.info("Selecting the Credit from the Type list.")
            activity_page.select_value_from_dropdown_text(activity_page.get_activity_type(), "Credit")
            log.info("Clicking the Go button.")
            activity_page.get_activity_button().click()
            transaction = activity_page.get_transaction_by_index(-1)
            log.info(f"Verifying if the transaction name is {activity_page.FUNDS_RECEIVED}")
            assert transaction[1] == activity_page.FUNDS_RECEIVED
            log.info(f"Verifying if the transaction amount is {amount}.")
            assert str(transaction[3]).split(".")[0] == amount

