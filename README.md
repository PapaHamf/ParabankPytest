## Table of contents
* [General info](#general-info)
* [Pre-requisites](...)
* [Technologies](#technologies)
* [Setup](#setup)

## General info
This a Parabank framework written in Python with Selenium. It contains various
test scenarios testing the basic functionality of the banking application.
The test suite contains the smoke test such as positive and negative customer
registration test, transfer funds test, customer login tests, account list test,
customer support form tests and bill payment tests.

## Pre-requisites
* ChromeDriver 131.0.6778.108+
* geckodriver 0.35.0+
* Microsoft Edge WebDriver 132.0.2957.41+
* Docker Parabank application

## Technologies
Project is created with:
* allure-pytest==2.13.5
* allure-python-commons==2.13.5
* ddt==1.7.2
* Faker==33.3.1
* JayDeBeApi==1.2.3
* openpyxl==3.1.5
* pytest==8.3.4
* pytest-html==4.1.1
* pytest_failed_screenshot==1.0.2
* selenium==4.27.1
	
## Setup
To setup the environment:

1. Install docker (ver. 26.1.3+).
2. Install the Chrome, Firefox & Edge browsers.
3. Download the proper chrome, gecko & edge drivers.
4. Install the docker parabank image.

To install the docker image:
```
$ ./docker_install.sh
```

To run the tests:

```
$ ./start_tests.sh
```

To run the tests via Jenkins:

```
$ ./jenkins.sh
```

