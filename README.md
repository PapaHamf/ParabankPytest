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
* apache-maven-3.9.9
* apache-tomcat-11.0.2
* ChromeDriver 131.0.6778.108
* geckodriver 0.35.0 
* Microsoft Edge WebDriver 132.0.2957.41
* Parabank application

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

1. Install the apache maven
2. Install the apache tomcat
3. Deploy the parabank application in apache tomcat
4. Install the Chrome, Firefox & Edge browsers
5. Download the proper chrome, gecko & edge drivers
6. Install the pre-requisites according to requirements.txt

To run the tests:

```
$ cd ParabankPytest
$ pytest 
$ allure serve allure-results
```

