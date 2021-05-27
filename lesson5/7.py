'''
Задание №7.
Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название,
форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).

Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
'''
import json
with open('text7.txt', 'r') as file:
    tmp = file.readlines()

i = 0
while i < len(tmp):
    tmp[i] = tmp[i].split()
    i += 1

result = []
summ_profit = 0
n = 1
i = 0
while  i < len(tmp):
	m = tmp[i]
	profit = int(m[2]) - int(m[3])
	list_f = m[0], profit
	#list_f_d= dict(list_f)
	print(1)
	print(list_f)
	print(1)
	result += list_f
	if profit > 0:
		summ_profit += profit
		n += 1
	i += 1
average_profit = ('average_profit', summ_profit / n)

final_list = [tuple(result), average_profit]

print(final_list)

