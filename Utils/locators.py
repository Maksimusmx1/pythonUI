# Локаторы для поиска
# Шаблон: "ID","Тип"(XPath,ClassName) ,"Описание локатора", "локатор"

def locators():
    locators = [(0, "XPath", "Геометка Москва", "//a[text()='Москва']")]
    #locators += [(1, "XPath", "Переключение языка", "//div[3]/a[text()='ENG']")]
    locators += [(1, "XPath", "Переключение языка", "//a[text()='ENG']")]
    locators += [(2, "ClassName", "Поиск 'Лупа'", "kitt-header-search")]
    locators += [(3, "XPath", "Страница Сбербанк Онлайн", "//a[text()='СберБанк Онлайн']")]
    locators += [(4, "XPath", "Страница ввода геолокации", "/html/body/div[4]/div/div/div[1]/input")]
    locators += [(5, "XPath", "Ссылка геолокации 'Ростовская область'", "//button[text()='Ростовская область']")]
    locators += [(6, "XPath", "Поле для ввода строки поиска", "//form/input[4]")]
    return locators
