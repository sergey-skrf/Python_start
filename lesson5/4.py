'''
Задание №4.
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться
в новый текстовый файл.
'''
buff1 = ['one','two','three','four','five']
buff2 = ['один','два','три','четыре','пять']

s=s.replace(buff1[i], buff2[i])
    f2.write(s)

with open('text4.txt', 'r') as file:
    tmp = file.readlines()
i = 0
while i < len(tmp):
    tmp[i] = tmp[i].split(' - ')
    i += 1
tmp_d = dict(tmp)
print(tmp_d)
tmp_d.pop('One')
tmp_d['Один'] = '1'
print(tmp_d)


