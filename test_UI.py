import pytest
from selenium import webdriver
import selenium
import requests

def test_UI():
    browser = webdriver.Chrome(r"C:\Program Files (x86)\ChromeDriverSB\sberbrowser_driver_2.0.0.0.exe")
    #browser = selenium.webdriver.Chrome("C:\Program Files (x86)\SberBrowser\Application\sberbrowser.exe").maximize_window()
    # чистим cookies
    browser.delete_all_cookies()
    # ожидаемое время для поиска элемента
    browser.implicitly_wait(10)
    browser.get("https://ya.ru/")
    browser.maximize_window()