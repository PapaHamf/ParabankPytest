import pytest
import allure

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from utils.DB_initialise import DataBaseInitialise
from utils.myfaker import MyFaker

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

# @pytest.fixture(params = ExcelData.get_excel_data("test_data.xlsx"))
#     def load_data(request):
#         """
#         Returns the data for parametrized (data driven) tests.
#         :return:
#         """
#         return request.param

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
    Set ups the environment for the tests.
    """
    # Purging the database and filling it w/ test data
    DBini = DataBaseInitialise()
    DBini.purge_database()
    DBini.populate_database()
    # Retrieving the value of the command line option
    match request.config.getoption("--browser-name"):
        case "chrome":
            chrome_options: ChromeOptions = webdriver.ChromeOptions()
            # chrome_options.add_argument("--headless")
            chrome_options.add_argument("--ignore-certificate-errors")
            driver = webdriver.Chrome(options = chrome_options)
        case "firefox":
            firefox_options: FirefoxOptions = webdriver.FirefoxOptions()
            firefox_options.add_argument("--headless")
            firefox_options.add_argument("--ignore-certificate-errors")
            driver = webdriver.Firefox(options = firefox_options)
        case "edge":
            edge_options: EdgeOptions = webdriver.EdgeOptions()
            edge_options.add_argument("--headless")
            edge_options.add_argument("--ignore-certificate-errors")
            driver = webdriver.Edge(options = edge_options)
    driver.implicitly_wait(5)
    request.cls.driver = driver
    yield driver
    driver.close()