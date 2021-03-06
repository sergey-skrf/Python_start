'''
Задание №5.
Реализовать формирование списка, используя функцию range() и возможности генератора. 
В список должны войти четные числа от 100 до 1000 (включая границы).

Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().
'''

# импортиреум reduce
from functools import reduce
# создаем список четных чисел в диапазоне от 100 по 1000
list_number = [itm for itm in range(100, 1001) if itm % 2 == 0]

# производим вычесление всех элементов списка с помощью reduce
multiplication = reduce(lambda a, x: a * x, list_number)
print(multiplication)



#Вариант решения преподавателя

from functools import reduce

result_list = [itm for itm in range(100, 1001) if not itm % 2]
result_composition = reduce(lambda x, y: x * y, result_list)