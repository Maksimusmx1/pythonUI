# импорт библиотеки для работы с наведением курсора мыши
from selenium.webdriver.common.action_chains import ActionChains
import time

def on_blur(element,driver):
    # Наведем на ссылку и подождем 5 секунд
    ActionChains(driver).move_to_element(element).perform()
    time.sleep(5)