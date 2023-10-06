# Функция печатает все найденные элементы по локатору
def elements_reports(elements):
    elements_count =  len(elements)
    print("Найдено элементов", elements_count)
    for i in range(elements_count):
        print("Элемент " + str(i), elements[i])