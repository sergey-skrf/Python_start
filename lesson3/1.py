'''
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. 
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
'''

def division_two_number():
	'''
	Возвращает результат деления двух чисел

	number_1, number_2 - позиционные оргументы
	(number_1, number_2) -> number
	'''

	number_1 = int(input('Введите делимое число\n'))
	number_2 = int(input('Введите делитель\n'))
	
	if number_2 == 0:
		return 'Делить на ноль нельзы'
	else:
		return number_1/number_2

print(division_two_number())




# Вариант решения преподавателя

def division(a: float, b: float):
	'''
	делит a на b
	:param a:
	:param b:
	:return: float or None
	'''
	try:
		return a / b
	except ZeroDivisionError as e:
		print('Нельзя делить на ноль')


division2 = lambda a, b: a / b if b else None

assert division(4, 2) == 2, 'division(4, 2)'


assert division2(4, 2) == 2, 'division(4, 2)'