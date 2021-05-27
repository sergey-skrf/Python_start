'''
Задание №3. 
Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
'''

with open('text3.txt', 'r') as file:
    tmp = file.readlines()

i = 0
while i < len(tmp):
    tmp[i] = tmp[i].split()
    tmp[i].reverse()
    i += 1
tmp_d = dict(tmp)

for itm in tmp_d.keys():
    if int(itm) < 20000:
        print(f'Оклад менее 20000 руб.:\n{tmp_d.setdefault(itm)}')

n = 0
for itm in tmp_d.keys():
    n += int(itm)
average_salary = n / len(tmp_d.keys())
print(f'Средняя величина заработной платы сотрудников составляет {average_salary} руб.')