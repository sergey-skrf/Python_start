'''
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.

Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса
Matrix (двух матриц).  Результатом сложения должна быть новая матрица.

Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы
складываем с первым элементом первой строки второй матрицы и т.д.
'''

class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return f'{self.matrix[0]}\n{self.matrix[1]}\n{self.matrix[2]}\n'

    def __add__(self, other):
        i = 0
        while i < len(self.matrix):
            n = 0
            while n < len(self.matrix[i]):
                self.matrix[i][n] = self.matrix[i][n] + other.matrix[i][n]
                n += 1
            #n = 0
            i += 1
        return Matrix(self.matrix)

mc1 = Matrix([[31, 22], [37, 43], [51, 100]])
mc2 = Matrix([[69, 78], [63, 57], [49, 99]])
print(mc1)
print(mc2)
print(mc1 + mc2)
