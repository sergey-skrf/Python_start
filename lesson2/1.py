""" 
Задание №1. Создать список и заполнить его элементами различных типов данных. 
Реализовать скрипт проверки типа данных каждого элемента. 
Использовать функцию type() для проверки типа. 
Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
"""
# задаём элементы списка
list_of_elements = [1, 'строка', True, {1}, (1,), [1]]

# проходим по элиментам списка и выводим на экран элементы списка с указанием их типа
for itm in list_of_elements:
	print(f'{itm} - {type(itm)}')