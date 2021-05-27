'''
Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс)
этого проекта — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто
и костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные
числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани.

Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
'''

class Clothes:
    def __init__(self):
        self.list_clothes = []

    def add_coat(self, size):
        self.list_clothes.append(Coat(size))

    def add_suit(self, height):
        self.list_clothes.append(Suit(height))

    @property
    def all_cloth(self):
        total_demand_of_fabric = 0
        for el in self.list_clothes:
            total_demand_of_fabric += el.full_cloth
        return f'Общая потребность ткани составляет: {total_demand_of_fabric}.'

class Coat:
    def __init__(self, size):
        self.full_cloth = size / 6.5 + 0.5

class Suit:
    def __init__(self, height):
        self.full_cloth = 2 * height + 0.3

r = Clothes()
r.add_coat(54)
r.add_suit(1.82)
#print(r.all_cloth())
print(r.all_cloth)
