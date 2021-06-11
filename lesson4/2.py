'''
Задание №2.
Представлен список чисел. Необходимо вывести элементы исходного списка, 
значения которых больше предыдущего элемента.

Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. 
Для формирования списка использовать генератор.
'''

list_number = [1, 5, 2, 8, 6, 12, 1, 5]
print(list_number)
i = 0
while i < (len(list_number) - 1):
	if int(list_number[i]) < int(list_number[i+1]):
		list_number.pop(i)
		i += 1
print(list_number)
print('*'*20)


#Вариант преподавателя

def test_iter(*args):
	prev = float('inf') * -1

	for idx, itm in enumerate(args):
		if itm > prev:
			yield itm
		prev = itm

list_number1 = [1, 5, 2, 8, 6, 12, 1, 5]
print(list_number1)

new_list = []
for itm in test_iter(*list_number1):
	new_list.append(itm)
print(new_list)


if __name__ == '__main__':
	assert list(test_iter(1, 2, 3, 4, 5, 6, 7, 8)) == [1, 2, 3, 4, 5, 6, 7, 8], 'one'
	assert list(test_iter(-1, 3, 6, 12, -5, 0, 2, 7)) == [-1, 3, 6, 12, 0, 2, 7], 'two'
	assert list(test_iter(1)) == [1], 'three'
	assert list(test_iter()) == [], 'four'