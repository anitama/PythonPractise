import pytest
from selenium import webdriver

@pytest.yield_fixture()
def setup():
    global driver
    driver=webdriver.Chrome("D:/Drivers/chromedriver_win32/chromedriver.exe")
    driver.maximize_window()
    driver.delete_all_cookies()
    driver.get("http://facebook.com")
    yield
    print("Execution completed")
    driver.quit()

def test_m4(setup):
    fbtitle = driver.title;
    print("Title is here",fbtitle)
    assert fbtitle == "Facebook – log in or sign up", "assertion failed"

def test_m3(setup):
    driver.find_element_by_id("email").send_keys("isita76@gmail.com")
    driver.find_element_by_id("pass").send_keys("iku7711")
    driver.find_element_by_xpath("//input[@value='Log In']").click()
    assert driver.title=="Facebook","assertion failed due to invalid title"

def test_m4(setup):
    print("Newly added Method in the class")


