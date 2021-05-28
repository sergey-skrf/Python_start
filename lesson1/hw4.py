'''Задание №4.
Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции
'''

number = int(input('Введите целое положительное число:\n'))
mod_number = str(number)
i = 0 # переменная счётчик
max_number = mod_number[0] #задаём, что самая большая цифра первая по порядку
while i < len(mod_number): # в цикле проводим сравнение цифр в числе, самое большое значение записываем в переменную max_number
	if max_number < mod_number[i]:
		max_number = mod_number[i]
		i += 1
	else:
		i += 1
print(max_number)





#Решение преподавателя
number = input('Введите целое положительное число:\n')
if number.isdigit():
	number = int(number)
	summury = 0
	big_num = 0
	while number:
		if number % 10 > big_num:
			big_num = number % 10
		summury += number % 10
		number //= 10
	print(f'Сумма равна: {summury}')
	print(f'Самая большая цифра: {big_num}')
else:
	print('Введено не число')