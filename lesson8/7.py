'''
Занаие №7.
Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.

Проверьте корректность полученного результата.
'''
class Complex_number:
    def __init__(self, complex_num):
        self.complex_num = complex_num

    def __add__(self, other):
        return Complex_number(self.complex_num + other.complex_num)

    def __mul__(self, other):
        return Complex_number(self.complex_num * other.complex_num)

    def __str__(self):
        return f"Объект с параметрами: {self.complex_num}"

mc_1 = Complex_number(complex(1, 2))
mc_2 = Complex_number(complex(3, 4))
print(mc_1 + mc_2)
print(mc_1 * mc_2)