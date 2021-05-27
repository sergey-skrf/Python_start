'''
Задание №2. 
Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
'''

my_file = open("text1.txt", "r")
list_lines = my_file.readlines()
quantity_line = len(list_lines)
print(f'Количество строк в файле {my_file.name} составляет: {quantity_line}')
for idx, itm in enumerate(list_lines, 1):
    print(f'Количество слов в строке № {idx} равно {len(itm.split())}')
my_file.close()