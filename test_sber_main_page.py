import pytest
from selenium import webdriver
import time
import Utils.selectors as selectors
# импорт библиотеки для работы с наведением курсора мыши
from selenium.webdriver.common.action_chains import ActionChains

def test_elements_sber_main_page():

    # print ("elem", driver.find_element_by_class_name('kitt-header-search'))
    # Поиск элемента с геометкой Москва
    geo_button = selectors.create_selectors(0, driver)
    # Выведем текст элемента
    print("Текст элемента ", geo_button[0].text)
    # Поиск элемента переключения языка
    selectors.create_selectors(1, driver)
    # Поиск элемента лупа
    selectors.create_selectors(2, driver)
    # Найдем элемент Сбербанк Он Лайн
    main_page = selectors.create_selectors(3, driver)
    # Наведем на ссылку и подождем 5 секунд
    ActionChains(driver).move_to_element(main_page[0]).perform()
    time.sleep(5)
    # Меняем регион
    geo_button[0].click()
    time.sleep(5)
    geo_field = selectors.create_selectors(4, driver)
    geo_field[0].send_keys("Вообще не область")
    time.sleep(5)
    geo_field[0].clear()
    geo_field[0].send_keys("Ростовская область")
    geo_field_link = selectors.create_selectors(5, driver)
    geo_field_link[0].click()
    # Найдем элемент Сбербанк Он Лайн т.к. после смены региона DOM модель поменялась
    main_page = selectors.create_selectors(3, driver)
    # Кликнем по ссылке
    main_page[0].click()


def test_dz_UI_2():
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
    # Сменим язык страницы на английский Закоментированы, т.к. открывают другое окно и оно активно!!!
    ## Найдем элемент смены языка
    #change_language = selectors.create_selectors(1, driver)
    ## Сменим язык (кликнем по ссылке)
    #change_language[0].click()
    # Поиск элемента лупа
    search_icon = selectors.create_selectors(2, driver)
    # кликнем по иконке поиска
    search_icon[0].click()
    # Ищем поле ввода поиска
    search_field = selectors.create_selectors(6, driver)
    # Ожидаем 5 секунд для прорисовки
    time.sleep(5)
    # Вводим в поле текст 'кредитный риск'
    search_field[0].send_keys("кредитный риск")
    # Ожидаем 10 секунд для прорисовки
    time.sleep(10)
