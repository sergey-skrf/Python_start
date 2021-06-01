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

#Варианты решения предложенные преподаватем

def my_func1(a, b, c):
	return max(a + b, b + c, c + a)

my_func2 = lambda a, b, c: max(a + b, b + c, c + a)


assert my_func1(1, 2, 3) == 5, 'my_func1(1, 2, 3)'
assert my_func1(-22, 3, 7) == 5, 'my_func1(-22, 3, 7)'

assert my_func2(1, 2, 3) == 5, 'my_func1(1, 2, 3)'
assert my_func2(-22, 3, 7) == 5, 'my_func1(-22, 3, 7)'