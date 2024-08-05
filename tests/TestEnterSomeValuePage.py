import pytest
import unittest
import utils.CustomLogger as cl
from pages.EnterSomeValuePage import EnterValue

@pytest.mark.usefixtures("beforeClass", "beforeMethod")
class TestEnterSomeValuePage(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.esp = EnterValue(self.driver)

    @pytest.mark.order(1)
    def test_openEnterValuePage(self):
        cl.allureLogs("App is Launched")
        self.esp.openEnterValuePage()
        self.esp.verifyIfPageDisplayed()
    
    @pytest.mark.order(2)
    def test_enterValue(self):
        self.esp.enterValue()
        self.esp.clickSubmitButton()