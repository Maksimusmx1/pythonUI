import pytest
from selenium import webdriver
import time
import Utils.selectors as selectors

def test_elements_sber_main_page():
    # Initialize Chrome WebDriver
    driver = webdriver.Chrome('C:\Program Files (x86)\ChromeDriverSB\sberbrowser_driver.exe')
    # чистим cookies
    driver.delete_all_cookies()
    # ожидаемое время для поиска элемента
    driver.implicitly_wait(10)
    # Открываем главную страницу
    driver.get("http://www.sberbank.ru/")
    # Раскрываем окно не полный экран
    driver.maximize_window()
    # Ожидаем 5 секунд для прорисовки
    time.sleep(5)
    # print ("elem", driver.find_element_by_class_name('kitt-header-search'))
    # Поиск элемента с геометкой Москва
    selectors.create_selectors(0, driver)
    # Поиск элемента переключения языка
    selectors.create_selectors(1, driver)
    # Поиск элемента лупа
    selectors.create_selectors(2, driver)



