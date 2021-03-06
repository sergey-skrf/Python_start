""" 
Задание №1. 
Реализовать скрипт, в котором должна быть предусмотрена функция 
расчета заработной платы сотрудника. В расчете необходимо использовать формулу: 
(выработка в часах * ставка в час) + премия. Для выполнения расчета для конкретных значений 
необходимо запускать скрипт с параметрами.
"""

# импортируем модуль sys
import sys

# по средствам sys.argv задаём значения переменным production, rate и prize
# production - выработка в часах
# rate - ставка в час
# prize - размер премии
_, production, rate, prize = sys.argv


print(f'Выработка {production} частов, ставка в час {rate} руб., премия {prize} руб.')

# создаём функцию расчёта заработной по формуле приведённой в задании
def salary(production, rate, prize):
    result = int(production) * int(rate) + int(prize)
    return result

print(f'Заработная плата составляет: {salary(production, rate, prize)} руб.')

# ожидаемый ввод в терминале для запуска скрипта: python 1.py 'выработка в часах' 'ставка в час' 'премия'