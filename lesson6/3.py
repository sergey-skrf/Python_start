'''
Реализовать базовый класс Worker (работник), в котором определить атрибуты:
name, surname, position (должность), income (доход).
Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
и дохода с учетом премии (get_total_income). 
Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, 
проверить значения атрибутов, вызвать методы экземпляров).
'''

class Worker:

	def __init__(self, name, surname, position):
		self.name = name
		self.surname = surname
		self.position = position
		self._income = {"wage": 50000, "bonus": 15000}
		

class Position(Worker):
	def __init__(self, name, surname, position):
		super().__init__(name, surname, position)
		
	def get_full_name(self):
		print(f'{self.name} {self.surname} - {self.position}')

	def get_total_income(self):
		#wage = self._income["wage"]
		#bonus = self._income["bonus"]
		print(f'Дохода с учетом премии: {self._income["wage"] + self._income["bonus"]}')	

a = Position('Сергей', 'Кисиль', 'python developer')
a.get_full_name()
a.get_total_income()
print(a.name)
print(a.surname)
print(a.position)
print(a._income['wage'])
print(a._income['bonus'])