'''
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, 
и возвращает сумму наибольших двух аргументов.
'''

def my_func(number_1, number_2, number_3):
	'''
	Возвращает сумму наибольших двух аргументов

	Позиционные аргументы:
	number_1, number_2, number_3 - числовые значения
	'''
	
	list_number = [number_1, number_2, number_3]
	list_number.sort()
	return list_number[1]+list_number[2]
	
print(my_func(10, 2, 9))
