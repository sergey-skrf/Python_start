'''Задание №3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3.
Счатаем 3 + 33 + 333 = 369'''

use_number = int(input('Введите число:\n'))
mod_use_number1 = int(str(use_number) * 2) #получаем число nn
mod_use_number2 = int(str(use_number) * 3) #получаем число nnn
sum_of_numbers = use_number + mod_use_number1 + mod_use_number2 #вычисляем сумму n + nn + nnn
print(sum_of_numbers)


#Варианты преподавателя
#1
user_number = input('Введите число')
if user_number.isdigit():
	result = int(user_number) + int(user_number * 2) + int(user_number * 3)
	print(result)

#2
user_number = input('Введите число')
count = 3
result = 0
while count and user_number.isdigit():
	result += int(user_number * count)
	count -= 1
print(result)