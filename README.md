# Mobile Automation Test Project

This project is designed to automate mobile application testing using Appium and Python. The project uses a page object model (POM) framework to organize and structure the test code.

## Project Structure

1. pages: This directory contains the page object classes for each screen in the mobile application.
2. tests: This directory contains the test classes for each feature in the mobile application.
3. utils: This directory contains utility classes for logging, driver management, and other helper functions.
4. config: This directory contains configuration files for the project, including the Appium server endpoint and desired capabilities.
5. reports: This directory contains the logs and reports for each page

## Setup

1. Clone the project repository using git clone.
2. Install the required dependencies using pip install -r requirements.txt.
3. Configure the Appium server endpoint and desired capabilities in config/android_config.py.
4. Run the tests using pytest tests/ in the command line.

## Test Execution

Tests can be executed using Pytest. To run all tests, navigate to the project root directory and execute pytest tests/. To run a specific test, execute pytest tests/test_name.py.

## Reporting

Test results are logged to the reports directory. The logs include detailed information about each test, including pass/fail status, error messages, and screenshots. allure-pytest is used for reporting.
To generate reports for TestEnterSomeValuePage.py file, run:

pytest -v -s --alluredir=/path/to/reports/folder TestEnterSomeValuePage.py

To start the allure server:

allure serve /path/to/reports/folder
