import random
class Homo:

	__population = 0

	def __init__(self, height, sex, age, weight, father=None, mother=None):
		self.height = height
		self.sex = sex
		self.age = age
		self.weight = weight
		self.father = father
		self.mother = mother
		self._ind = weight / (height**2)
		self.__duble_ind = self._ind ** 2
		Homo.__population += 1


	def say(self):
		print('HEYYYYY')


	@classmethod
	def population(cls):
		print(cls.__population)


	def say_duble_ind(self):
		print(self.__duble_ind)


class Human(Homo):

	def __init__(self, height, sex, age, weight, name, surname, father=None, mother=None):
		self.name = name
		self.surname = surname
		super().__init__(height, sex, age, weight, father, mother)

	def say2(self):
		print(self._ind)

	def say(self):
		print(f'my name is {self.name} {self.surname}')



	def reproduction(self, mother):

		'''
		:param mother: Human
		:return: Human
        '''
		return Human(
			height=20,
			sex=random.choice(('w', 'm')),
			age=0,
			weight=3.600,
			name=mother.name,
			surname=self.surname,
			father=self,
			mother=mother)





if __name__ == '__main__':
	dasha = Human(170, 'w', 22, 55, 'Даша', 'Иванова')
	print(1)
	petr = Human(170, 'm', 22, 55, 'Петр', 'Иванов')
	child = petr.reproduction(dasha)
