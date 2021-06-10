'''
Задание №6. 
Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение. 
При вызове функции должен создаваться объект-генератор. 
Функция должна вызываться следующим образом: for el in fibo_gen(). 
Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые 15 чисел.

Подсказка: факториал числа n — произведение чисел от 1 до n. 
Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.
'''

# создаем функцию расчёта факториала с ключевым словом yield (создаем генератор)
def fibo_gen(number):
    factorial = 1
    while number > 1:
        factorial *= number
        number -= 1
    yield factorial

# вызываем функцию
for el in fibo_gen(15):
    print(el)





#Вариант решения преподавателя

from functools import reduce

def fido_gen1():
    factor = 1
    while True:
        if factor > 1:
            yield reduce(lambda x, y: x * y, range(1, factor+1))
        else:
            yield 1
        factor += 1


if __name__ == '__main__':
    for idx, num in enumerate(fido_gen1(), start=1):
        print(idx, num)
        if idx == 15:
            break

