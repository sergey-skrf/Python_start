'''
6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же, 
но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.

Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом. 
Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки, 
но каждое слово должно начинаться с заглавной буквы. 
Необходимо использовать написанную ранее функцию int_func().
'''

def int_func(user_data):
	'''
	Принимает слово из маленьких букв и возвращающую его же, но с прописной первой буквой

	Позиционные аргументы:
	user_data - строка

	str --> ыек 
	'''
	return user_data.title()


user_data = 'хочу расти'
new_list = []

for el in user_data.split():
	new_list.append(int_func(el))

print(' '.join(new_list))


#Вариант решения преподавателя

def int_func1(string: str):
	return ''.join((string[0].upper(), string[1:])) if string else string

def user_temp(string: str):
	return ' '.join(map(int_func1, string.split(' ')))

print(user_temp('вот так'))