'''
5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. 
При нажатии Enter должна выводиться сумма чисел. 
Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter. 
Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме. 
Но если вместо числа вводится специальный символ, выполнение программы завершается. 
Если специальный символ введен после нескольких чисел, 
то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.
'''

import re
summ = 0

def my_func(user_data):
	'''
	Выводит сумму чисел, которые вводит пользователь через пробел

	Позиционные аргументы:
	user_data - строка

	str --> int 
	'''

	global summ
	user_data_list = user_data.split()
	for el in user_data_list:
		if el.isdigit():
			summ += int(el)
		else:
			break
	print(summ)



user_data = input('Введите строку чисел, разделенных пробелом:\n')
regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
while regex.search(user_data) == None:
	my_func(user_data)
	user_data = input('Введите строку чисел, разделенных пробелом:\n')
else:
	my_func(user_data)


#Вариант преподователя

def insert_sum(*args):
	result = 0
	exit_flag = False
	try:
		for itm in args:
			result += float(itm) if itm else 0
	except ValueError as e:
		exit_flag = not exit_flag
	return result, exit_flag

user_sum = 0
while True:
	user_input = input('Введите число').split(' ')
	result_sum, user_exit = insert_sum(*user_input)
	user_sum += result_sum
	print(user_sum)

	if user_exit:
		print('Досвидания')
		break