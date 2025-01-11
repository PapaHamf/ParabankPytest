import pytest

from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--ignore-certificate-errors")

# Hook for command line options
def pytest_addoption(parser):
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
    # Retrieving the value of the command line option
    match request.config.getoption("--browser-name"):
        case "chrome":
            driver = webdriver.Chrome(options=chrome_options)
        case "firefox":
            driver = webdriver.Firefox(options=chrome_options)
        case "edge":
            driver = webdriver.Edge(options=chrome_options)
    driver.implicitly_wait(5)
    request.cls.driver = driver
    yield
    driver.close()