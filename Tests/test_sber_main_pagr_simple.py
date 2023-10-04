import Utils.initial as initial
import pytest
import Steps.assert_steps as assert_steps

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
    search_icon = driver.find_elements_by_class_name("kitt-header-search")
    # Проверим, что элемент нашли
    assert_steps.assert_element_not_null(search_icon)


