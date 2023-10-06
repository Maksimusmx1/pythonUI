from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options

# инициализируем webdriver и устанавливаем переменные
def webdriver_init():
    # Initialize Chrome WebDriver
    # options = Options()
    # options.add_argument('--cert-file=' + '../cert/russian_trusted_root_ca.cer')
    # driver = webdriver.Chrome('C:\Program Files (x86)\ChromeDriverSB\sberbrowser_driver.exe', chrome_options=options)
    driver = webdriver.Chrome('C:\Program Files (x86)\ChromeDriverSB\sberbrowser_driver.exe')
    webdriver.ChromeOptions().add_argument('ignore-certificate-errors')
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
    return driver