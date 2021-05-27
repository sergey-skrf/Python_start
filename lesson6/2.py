'''
Задание №2. 
Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина). 
Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными. 
Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна. Использовать формулу: длинаширинамасса асфальта 
для покрытия одного кв метра дороги асфальтом, толщиной в 1 см*число см толщины полотна. Проверить работу метода.
Например: 20м*5000м*25кг*5см = 12500 т
'''
class Road:
	# атрибуты
	_length = 5000
	_width = 20


	# метод
	def mass_of_asphalt(self, mass_of_asphalt_in_1m2, layer_thickness):
		self.mass_of_asphalt_in_1m2 = mass_of_asphalt_in_1m2
		self.layer_thickness = layer_thickness
		_length = Road._length
		_width = Road._width
		mass_of_asphalt = _length * _width * mass_of_asphalt_in_1m2 / 1000 * layer_thickness / 100
		print(f'Масса асфальта, необходимого для покрытия всего дорожного полотна равна {mass_of_asphalt} т')
	
a = Road()
a.mass_of_asphalt(25, 5)

