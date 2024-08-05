
from appium.webdriver.common.appiumby import AppiumBy

def scroll(driver, text):
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, f'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("{text}").instance(0))')