import time
import pytest

from utils.driver import Driver

@pytest.fixture(scope='class')
def setUpClass(request):
    driver = Driver().get_driver()
    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    time.sleep(4)
    driver.quit()

@pytest.fixture()
def setUpMethod():
    print("Before Method")
    yield
    print("After Method")
