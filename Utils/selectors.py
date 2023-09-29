import Utils.locators as locators
from selenium import webdriver

# Селекторы выбора элемента для UI. Driver передается, чтобы не открывать дополнительных окон
def create_selectors(id, driver):
    # Локатор состоит из: ID[0] , Тип[1], Описание[2], Локатор[3]
    # Выбираем нужный локатор
    locator = locators.locators()[id]
    print("locators ", locator)
    print("type ", type(locator))
    print("0 ", locator[0])
    print("1 ", locator[1])
    print("2 ", locator[2])
    print("3 ", locator[3])
    # Выдаем сообщение пользователю
    print("Ищем элемент '" + locator[2] + "' методом '" + locator[1] +"'")
    # В зависимости от Типа ищем Элемент
    if locator[1] == 'XPath':
        element = driver.find_elements_by_xpath(locator[3])
    elif locator[1] == 'ClassName':
        # Т.к. для className возвращаемый тип не list, сделаем его таковым
        #element = []
        #element.append(driver.find_element_by_class_name(locator[3]))
        element = driver.find_elements_by_class_name(locator[3])
    # Проверим, сколько элементов найдено с выбранным локатором
    print("element", element)
    print("Type element = ", type(element))
    print("Нашли " + str(len(element)) + " элемент(ов,а)")
    return element



