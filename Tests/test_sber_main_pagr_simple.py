import Utils.initial as initial
import Steps.assert_steps as assert_steps
import time
import Steps.blur_steps as blur_steps
from selenium.webdriver.common.keys import Keys

def test_sber_main_page_dz_2():
    # Иницилизируем webdriver
    driver = initial.webdriver_init()
    # Поиск элемента с геометкой Москва
    geo_button = driver.find_element_by_xpath("//a[text()='Москва']")
    # Проверим, что элемент нашли
    assert_steps.assert_element_not_null(geo_button)
    # Поиск элемента переключения языка
    language_change = driver.find_element_by_xpath("//a[text()='ENG']")
    # Проверим, что элемент нашли
    assert_steps.assert_element_not_null(language_change)
    # Поиск элемента лупа
    search_icon = driver.find_element_by_class_name("kitt-header-search")
    # Проверим, что элемент нашли
    assert_steps.assert_element_not_null(search_icon)

# Тест переключения языка
def test_sber_main_page_dz_3_1():
    # Иницилизируем webdriver
    driver = initial.webdriver_init()
    # Поиск элемента переключения языка
    language_change = driver.find_element_by_xpath("//a[text()='ENG']")
    # Проверим, что элемент нашли
    assert_steps.assert_element_not_null(language_change)
    # Кликнем по ссылке "ENG"
    language_change.click()
    # Подождем 5 секунд для прописовки страницы
    time.sleep(5)

# Тест поиска
def test_sber_main_page_dz_3_2():
    # Иницилизируем webdriver
    driver = initial.webdriver_init()
    # Поиск элемента лупа
    search_icon = driver.find_element_by_class_name("kitt-header-search")
    # Проверим, что элемент нашли
    assert_steps.assert_element_not_null(search_icon)
    # кликнем по иконке поиска
    search_icon.click()
    # Ищем поле ввода поиска
    search_field = driver.find_element_by_xpath("//form/input[4]")
    # Проверим, что элемент нашли
    assert_steps.assert_element_not_null(search_icon)
    # Ожидаем 5 секунд для прорисовки
    time.sleep(5)
    # Зададим переменную и присвоим значение, которое будем искать
    search_value = "кредитный риск"
    # Вводим в поле текст
    search_field.send_keys(search_value)
    # Ожидаем 5 секунд для прорисовки
    time.sleep(5)
    # Ищем элемент
    search_link = driver.find_element_by_xpath("//a[text()='" + search_value + "']")
    # Проверим, что элемент нашли
    assert_steps.assert_element_not_null(search_link)
    # Перейдем по ссылке
    search_link.click()
    # Закроем страницу
    driver.close()

# Тест поиска негативный сценарий
def test_sber_main_page_dz_3_2_negative():
    # Иницилизируем webdriver
    driver = initial.webdriver_init()
    # Поиск элемента лупа
    search_icon = driver.find_element_by_class_name("kitt-header-search")
    # Проверим, что элемент нашли
    assert_steps.assert_element_not_null(search_icon)
    # кликнем по иконке поиска
    search_icon.click()
    # Ищем поле ввода поиска
    search_field = driver.find_element_by_xpath("//form/input[4]")
    # Проверим, что элемент нашли
    assert_steps.assert_element_not_null(search_icon)
    # Зададим переменную и присвоим значение, которое будем искать
    search_value = "вообще не продукт"
    # Вводим в поле текст
    search_field.send_keys(search_value)
    # Ожидаем 5 секунд для прорисовки
    time.sleep(5)
    # Ищем элемент
    search_link = driver.find_elements_by_xpath("//a[text()='" + search_value + "']")
    # Прверим, что элемента не нашли
    assert_steps.assert_element_is_null(search_link)

# Тест наведения на элемент
def test_sber_main_page_dz_3():
    # Иницилизируем webdriver
    driver = initial.webdriver_init()
    # Поиск элемента курсы валют
    exchange = driver.find_element_by_xpath("//a[text()='Курсы валют']")
    # Проверим, что элемент нашли
    assert_steps.assert_element_not_null(exchange)
    # Наведем на ссылку и подождем 5 секунд
    blur_steps.on_blur(exchange, driver)
    # Поиск элемента офисы
    offices = driver.find_element_by_xpath("//header/div/div[2]/div[2]/a[2]")
    # Проверим, что элемент нашли
    assert_steps.assert_element_not_null(offices)
    # Наведем на ссылку и подождем 5 секунд
    blur_steps.on_blur(offices, driver)
    # Поиск элемента банкоматы
    cashoffice = driver.find_element_by_xpath("//header/div/div[2]/div[2]/a[3]")
    # Проверим, что элемент нашли
    assert_steps.assert_element_not_null(cashoffice)
    # Наведем на ссылку и подождем 5 секунд
    blur_steps.on_blur(cashoffice, driver)
    # Поиск элемента с геометкой Москва
    geo_button = driver.find_element_by_xpath("//a[text()='Москва']")
    # Проверим, что элемент нашли
    assert_steps.assert_element_not_null(geo_button)
    # Наведем на ссылку и подождем 5 секунд
    blur_steps.on_blur(geo_button, driver)
    # Поиск элемента переключения языка
    language_change = driver.find_element_by_xpath("//a[text()='ENG']")
    # Проверим, что элемент нашли
    assert_steps.assert_element_not_null(language_change)
    # Наведем на ссылку и подождем 5 секунд
    blur_steps.on_blur(language_change, driver)
    # Поиск элемента лупа
    search_icon = driver.find_element_by_class_name("kitt-header-search")
    # Проверим, что элемент нашли
    assert_steps.assert_element_not_null(search_icon)
    # Наведем на ссылку и подождем 5 секунд
    blur_steps.on_blur(search_icon, driver)

# Тест нскроллинга
def test_sber_main_page_dz_4():
    # Иницилизируем webdriver
    driver = initial.webdriver_init()
    # Найдем элемент body
    body_element = driver.find_element_by_tag_name('body')
    # Ожидаем 5 секунд для прорисовки
    time.sleep(5)
    # Прокрутим страницу вниз
    body_element.send_keys(Keys.PAGE_DOWN)
    # Ожидаем 5 секунд для прорисовки
    time.sleep(5)
    # Опустимся до footer'a
    body_element.send_keys(Keys.END)
    # Ожидаем 5 секунд для прорисовки
    time.sleep(5)
    # Поднимимся на на экран вверх
    body_element.send_keys(Keys.PAGE_UP)
    # Ожидаем 5 секунд для прорисовки
    time.sleep(5)
    # Поднимимся до header'a
    body_element.send_keys(Keys.HOME)
    # Ожидаем 5 секунд для прорисовки
    time.sleep(5)
    # сменим язык (произойдет открытие новой вкладки)
    # Поиск элемента переключения языка
    language_change = driver.find_element_by_xpath("//a[text()='ENG']")
    # Проверим, что элемент нашли
    assert_steps.assert_element_not_null(language_change)
    # Кликнем по ссылке "ENG"
    language_change.click()
    # Подождем 5 секунд для прописовки страницы
    time.sleep(5)
    # Переключимся на начальную вкладку
    driver.switch_to.window(driver.window_handles[0])
    # Ожидаем 5 секунд для прорисовки
    time.sleep(5)
    # Переключимся на начальную вкладку
    driver.switch_to.window(driver.window_handles[1])
    # Ожидаем 5 секунд для прорисовки
    time.sleep(5)