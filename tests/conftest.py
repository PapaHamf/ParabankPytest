import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from utils.DB_initialise import DataBaseInitialise

# Hook for command line options
def pytest_addoption(parser) -> None:
    parser.addoption("--browser-name",
                     action="store",
                     default="chrome",
                     help="Lets you choose one of the available drivers.")

# Fixture for command line option
@pytest.fixture
def browser_name(request):
    return request.config.getoption("--browser-name")


@pytest.fixture(scope="class")
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
            driver = webdriver.Chrome(options=chrome_options)
        case "firefox":
            firefox_options: FirefoxOptions = webdriver.FirefoxOptions()
            firefox_options.add_argument("--headless")
            firefox_options.add_argument("--ignore-certificate-errors")
            driver = webdriver.Firefox(options=firefox_options)
        case "edge":
            edge_options: EdgeOptions = webdriver.EdgeOptions()
            edge_options.add_argument("--headless")
            edge_options.add_argument("--ignore-certificate-errors")
            driver = webdriver.Edge(options=edge_options)
    driver.implicitly_wait(5)
    request.cls.driver = driver
    yield driver
    driver.close()