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