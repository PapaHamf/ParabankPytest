import pytest
import allure

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from utils.DB_initialise import DataBaseInitialise
from utils.myfaker import MyFaker
from utils.csvdata import CSVData
from utils.jsondata import JSONData
from utils.exceldata import ExcelData

# Hook for command line options
def pytest_addoption(parser) -> None:
    parser.addoption("--browser-name",
                     action = "store",
                     default = "chrome",
                     help = "Lets you choose one of the available drivers.")

# Fixture for command line option
@pytest.fixture
def browser_name(request):
    return request.config.getoption("--browser-name")

@pytest.fixture(scope = "function", params  = ExcelData.get_excel_data("dataset_customer.xlsx"))
def get_excel_data_customer_logins(request) -> list[dict]:
    """
    Returns the customer login data for parametrized (data driven) tests.
    :return: List containing the dictionaries w/ data.
    """
    return request.param

@pytest.fixture(scope = "function", params = ExcelData.get_excel_data("test_data_register_strings_too_short.xlsx"))
def get_excel_data_strings_too_short(request) -> list[dict]:
    """
    Returns the data w/ too short values for parametrized (data driven) tests.
    :return: List containing the dictionaries w/ data.
    """
    return request.param

@pytest.fixture(scope = "function", params = ExcelData.get_excel_data("test_data_register_strings_too_long.xlsx"))
def get_excel_data_strings_too_long(request) -> list[dict]:
    """
    Returns the data w/ too long values for parametrized (data driven) tests.
    :return: List containing the dictionaries w/ data.
    """
    return request.param

@pytest.fixture(scope = "function", params = CSVData.get_csv_data("test_data_register_strings_digits.csv"))
def get_csv_data_strings_added_digits(request) -> list[dict]:
    """
    Returns the data w/ random digits for parametrized (data driven) tests.
    :return: List containing the dictionaries w/ data.
    """
    return request.param

@pytest.fixture(scope = "function", params = CSVData.get_csv_data("test_data_register_strings_special.csv"))
def get_csv_data_strings_added_special(request) -> list[dict]:
    """
    Returns the data w/ special characters for parametrized (data driven) tests.
    :return: List containing the dictionaries w/ data.
    """
    return request.param

@pytest.fixture(scope = "function", params = CSVData.get_csv_data("test_data_homepage_footer_links.csv"))
def get_csv_data_footer_links(request) -> list[dict]:
    """
    Returns the data w/ footer links for parametrized (data driven) tests.
    :return: List containing the dictionaries w/ data.
    """
    return request.param

@pytest.fixture(scope = "function", params = JSONData.get_json_data("test_data_register_numbers_letters.json"))
def get_json_data_numbers_letters(request) -> list[dict]:
    """
    Returns the data w/ letters in numerical fields for parametrized (data driven) tests.
    :return: List containing the dictionaries w/ data.
    """
    return request.param

@pytest.fixture(scope = "function", params = JSONData.get_json_data("test_data_register_numbers_too_short.json"))
def get_json_data_numbers_too_short(request) -> list[dict]:
    """
    Returns the data w/ too short values for parametrized (data driven) tests.
    :return: List containing the dictionaries w/ data.
    """
    return request.param

@pytest.fixture(scope = "function", params = JSONData.get_json_data("test_data_register_numbers_too_long.json"))
def get_json_data_numbers_too_long(request) -> list[dict]:
    """
    Returns the data w/ too long values for parametrized (data driven) tests.
    :return: List containing the dictionaries w/ data.
    """
    return request.param

@pytest.fixture(scope = "function", params = JSONData.get_json_data("test_data_register_numbers_specials.json"))
def get_json_data_numbers_special(request) -> list[dict]:
    """
    Returns the data w/ special characters for parametrized (data driven) tests.
    :return: List containing the dictionaries w/ data.
    """
    return request.param

@pytest.fixture(scope = "function", params = MyFaker.customer_data_one_empty_field())
def get_customer_data_negative(request) -> list[dict]:
    """
    Returns the fake customer data w/ one element missing (empty) in each dictionary.
    :return: List containing the dictionaries w/ generated user data.
    """
    return request.param

@pytest.fixture(scope = "function", params = MyFaker.customer_data_all_fields())
def get_customer_data_positive(request) -> list[dict]:
    """
    Returns the fake customer data w/ all valid fields in each dictionary.
    :return: List containing the dictionaries w/ generated user data.
    """
    return request.param

@pytest.fixture(scope = "class")
@allure.title("Setting up the environment")
def setup(request):
    """
    Set-ups the environment for the tests.
    """
    # Purging the database and filling it w/ test data
    with allure.step("Step 1: Initializing the database"):
        DBini = DataBaseInitialise()
        DBini.purge_database()
        DBini.populate_database()
    # Retrieving the value of the command line option
    with allure.step("Step 2: Initializing the driver"):
        match request.config.getoption("--browser-name"):
            case "chrome":
                chrome_options: ChromeOptions = webdriver.ChromeOptions()
                #chrome_options.add_argument("--headless")
                chrome_options.add_argument("--ignore-certificate-errors")
                driver = webdriver.Chrome(options = chrome_options)
            case "firefox":
                firefox_options: FirefoxOptions = webdriver.FirefoxOptions()
                #firefox_options.add_argument("--headless")
                firefox_options.add_argument("--ignore-certificate-errors")
                driver = webdriver.Firefox(options = firefox_options)
            case "edge":
                edge_options: EdgeOptions = webdriver.EdgeOptions()
                #edge_options.add_argument("--headless")
                edge_options.add_argument("--ignore-certificate-errors")
                driver = webdriver.Edge(options = edge_options)
        driver.maximize_window()
        driver.implicitly_wait(5)
        request.cls.driver = driver
    yield driver
    with allure.step("Step 3: Closing the driver"):
        driver.quit()