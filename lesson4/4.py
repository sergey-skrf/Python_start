'''
Задание №4.
Представлен список чисел. 
Определить элементы списка, не имеющие повторений. 
Сформировать итоговый массив чисел, соответствующих требованию. 
Элементы вывести в порядке их следования в исходном списке.

Для выполнения задания обязательно использовать генератор.
'''

list_number = [1, 2, 4, 5, 6, 2, 5, 2]

used = set()
unique = [x for x in list_number if x not in used and (used.add(x) or True)]
print(unique)




#Вариант предложенный преподавателем
#1
def unique_gen(*args):
	for itm in args:
		if args.count(itm) == 1:
			yield itm

#2
test_list = [1, 2, 3, 4, 5, 1, 4, 3, 6, 3]
result = [itm for int in test_list if test_list.count(itm) == 1]