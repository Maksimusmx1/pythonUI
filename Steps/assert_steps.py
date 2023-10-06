import allure

# Функия проверяет, что элемент найден
def assert_element_not_null(response):
    with allure.step("Функия проверяет, что что элемент найден"):
        assert response is not None
        print("Элемент найден PASSED")

# Функия проверяет, что элемент отсутствует
def assert_element_is_null(response):
    with allure.step("Функия проверяет, что что элемент не найден"):
        # Тип response будет list, проверим, что это кустой список
        assert len(response) == 0
        print("Элемент не найден PASSED")