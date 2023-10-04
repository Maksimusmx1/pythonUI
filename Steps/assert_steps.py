import allure

# Функия проверяет, что элемент найден
def assert_element_not_null(response):
    with allure.step("Функия проверяет, что что элемент найден"):
        assert response is not None
        print("PASSED")