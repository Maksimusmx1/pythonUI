# Локаторы для поиска
# Шаблон: "ID","Тип"(XPath,ClassName) ,"Описание локатора", "локатор"

def locators():
    locators = [(0, "XPath", "Геометка Москва", "//a[text()='Москва']")]
    locators += [(1, "XPath", "Переключение языка", "//div[3]/a[text()='ENG']")]
    locators += [(2, "ClassName", "Переключение языка", "kitt-header-search")]
    return locators
