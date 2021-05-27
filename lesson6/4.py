'''
Задание №3. 
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево). 
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда). 
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed, 
который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed. 
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. 
Выполните вызов методов и также покажите результат.
'''
class Car:
	def __init__(self, speed, color, name, is_police):
		self.speed = speed
		self.color = color
		self.name = name
		self.is_police = is_police

	def show_speed(self):
		print (f'Скорость автомобиля {self.name} равна {self.speed}.')

	def go(self):
		print(f'Автомобиль {self.name} поехал. Цвет {self.color}')

	def stop(self):
		print(f'Автомобиль {self.name} остановился.')

	def turn(self, direction):
		print(f'Автомобиль {self.name} повернул на {direction}')

class TownCar(Car):

	def __init__(self, speed, color, name, is_police):
		super().__init__(speed, color, name, is_police)


	def show_speed(self):
		if self.speed > 60:
			print (f'Скорость автомобиля {self.name} равна {self.speed}. Вы превышаете скорость.')

class SportCar(Car):

	def __init__(self, speed, color, name, is_police):
		super().__init__(speed, color, name, is_police)


class WorkCar(Car):

	def __init__(self, speed, color, name, is_police):
		super().__init__(speed, color, name, is_police)

	def show_speed(self):
		if self.speed > 40:
			print (f'Скорость автомобиля {self.name} равна {self.speed}. Вы превышаете скорость.')


class PoliceCar(Car):

	def __init__(self, speed, color, name, is_police):
		super().__init__(speed, color, name, is_police)



a = Car(60, "черный", 'T-34', False)
a.go()
a.turn('право')
a.show_speed()
a.stop()
print(a.color)
print(a.is_police)

b = TownCar(61, "серый", 'T-72', False)
b.go()
b.turn('лево')
b.show_speed()
b.stop()
print(b.color)
print(b.is_police)

c = WorkCar(41, "хакки", 'T-80', False)
c.go()
c.turn('право')
c.show_speed()
c.stop()
print(c.color)
print(c.is_police)

c = SportCar(150, "red", 'T-90М', False)
c.go()
c.turn('право')
c.show_speed()
c.stop()
print(c.color)
print(c.is_police)

c = PoliceCar(150, "белый", 'T-90М', True)
c.go()
c.turn('право')
c.show_speed()
c.stop()
print(c.color)
print(c.is_police)