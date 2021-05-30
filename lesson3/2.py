'''
2. Реализовать функцию, принимающую несколько параметров, 
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон. 
Функция должна принимать параметры как именованные аргументы. 
Реализовать вывод данных о пользователе одной строкой.
'''

def user_data(name, surname, yeas_old, city, email, phone):
	'''
	Выводит данные о пользователе одной строкой

	Именованные аргументы:
	name     - имя пользователя
	surname  - фамилия пользователя
	yeas_old - возраст пользователя
	city     - город проживания
	email    - адре электронной почты
	phone    - телефон
	'''
	print (f'{name} {surname} {yeas_old}  {city} {email} {phone}')


user_data(name='Сергей', surname='Кисиль', yeas_old=33, city='New-York', email='ser@mail.ru', phone=9132511727)


# Вариант решения преподавателя
#1

def user_data1(name: str, surname: str, birth_year: int, city: str, email: str, phone: int):
	'''
	:param name: str
	:param surname: str
	:param birth_year: int
	:param city: str
	:param email: str
	:param phone: int
	:return: None
	'''
	return f'{name} {surname} {birth_year} года рождения, в городе {city}. Контакты: {email}, {phone}'

#2

def user_data_kw(**kwargs) -> str:
	'''
	Отображает данные о пользователе на экране
	:param name: str
	:param surname: str
	:param birth_year: int
	:param city: str
	:param email: str
	:param phone: int
	:return: str
	'''
	name = kwargs.get('name') or ''
	surname: kwargs.get('surname') or ''
	birth_year: kwargs.get('birth_year') or ''
	city: kwargs.get('city') or ''
	email: kwargs.get('email') or ''
	phone: kwargs.get('phone') or ''
	
	return f'{name} {surname} {birth_year} года рождения, в городе {city}. Контакты: {email}, {phone}'



user_data2 = lambda name, surname, birth_year, city, email, phone: f'{name} {surname} {birth_year} года рождения, в городе {city}. Контакты: {email}, {phone}'S