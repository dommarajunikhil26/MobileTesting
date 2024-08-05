from os import wait
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver
    
    def waitForElement(self, locatorValue, locatorType):
        locatorType = locatorType.lower()

        wait = WebDriverWait(self.driver, 20, poll_frequency=1, ignored_exceptions=[ElementNotSelectableException, ElementNotVisibleException, NoSuchElementException])
        if locatorType == 'id':
            element = wait.until(lambda x : x.find_element(AppiumBy.ID, locatorValue))
        elif locatorType == 'accessibility_id':
            element = wait.until(lambda x : x.find_element(AppiumBy.ACCESSIBILITY_ID, locatorValue))
        elif locatorType == 'classname':
            element = wait.until(lambda x : x.find_element(AppiumBy.CLASS_NAME, locatorValue))
        elif locatorType == 'text':
            element = wait.until(lambda x : x.find_element(AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("{locatorValue}")'))
        elif locatorType == 'index':
            element = wait.until(lambda x : x.find_element(AppiumBy.CLASS_NAME, f'new UiSelector().index({locatorValue})'))
        elif locatorType == 'desc':
            element = wait.until(lambda x : x.find_element(AppiumBy.CLASS_NAME, f'new UiSelector().description("{locatorValue}")'))
        elif locatorType == 'xpath':
            element = wait.until(lambda x : x.find_element(AppiumBy.XPATH, locatorValue))
        else:
            element = None
        return element
    
    def clickElement(self, locatorValue, locatorType="id",):
        try:
            locatorType = locatorType.lower()
            element = self.waitForElement( locatorValue, locatorType)
            element.click()
        except:
            print("error while clicking")
    
    def sendKeys(self, text,  locatorValue, locatorType="id"):
        try:
            locatorType = locatorType.lower()
            element = self.waitForElement(locatorValue, locatorType)
            element.send_keys(text)
        except:
            print("error while sending keys")
    
    def isElementDisplayed(self, locatorValue, locatorType="id"):
        try:
            locatorType = locatorType.lower()
            element = self.waitForElement(locatorValue, locatorType)
            element.is_displayed()
            return True
        except:
            print("print element not displayed")
            return False
