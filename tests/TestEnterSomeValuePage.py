import pytest
import unittest

from pages.EnterSomeValuePage import EnterValue

@pytest.mark.usefixtures("beforeClass", "beforeMethod")
class TestEnterSomeValuePage(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.Esp = EnterValue(self.driver)

    @pytest.mark.order(1)
    def test_launchApp(self):
        self.Esp.openEnterValuePage()
        self.Esp.verifyIfPageDisplayed()
    
    @pytest.mark.order(2)
    def test_enterValue(self):
        self.Esp.enterValue()
        self.Esp.clickSubmitButton()