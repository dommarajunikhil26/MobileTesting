from appium import webdriver
from appium.options.android import UiAutomator2Options
from config.android_config import desired_capabilities as android_caps, appium_server_url as android_url

class Driver:
    def get_driver(self):
        driver = webdriver.Remote(android_url, UiAutomator2Options().load_capabilities(android_caps))
        return driver



