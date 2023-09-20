import pytest
from selenium import webdriver
import time

def test_elements_sber_main_page():
    # Initialize Chrome WebDriver
    driver = webdriver.Chrome('C:/Program Files (x86)/ChromeDriverSB/sberbrowser_driver_2.0.0.0.exe')
    # чистим cookies
    driver.delete_all_cookies()
    # ожидаемое время для поиска элемента
    driver.implicitly_wait(10)
    driver.get("http://www.sberbank.ru/")
    driver.maximize_window()
    time.sleep(5)