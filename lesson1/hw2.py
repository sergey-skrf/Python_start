'''Задание №2.
Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматированеи строк
'''

time_in_seconds = int(input('Введите время в секундах:\n'))
hours = time_in_seconds // 3600 #вычисление количесива часов
minutes = time_in_seconds % 3600 // 60 #вычисление количества минут
seconds = time_in_seconds % 3600 % 60 #вычисление количества секунд
time = ('{}:{}:{}').format(hours, minutes, seconds)
print(time)



#запросим секунды у пользователя
user_sec = input('Введите время в секундах:\n')

#проверим что введено число
if user_sec.isdigit():
	#преобразуем строку в число
	user_sec = int(user_sec)

	#вычисляем заначения
	hours = user_sec // 3600
	minutes = user_sec % 3600 // 60
	seconds = user_sec % 3600 % 60

	#собираем строку результатов
	result = f'{hours:02}:{minutes:02}:{seconds:02}'
	print(result)
else:
	print('Введено ни число')