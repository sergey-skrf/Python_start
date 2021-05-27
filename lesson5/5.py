'''
Задание №5.
Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
'''

my_file = open("text5.txt", "w")
number_list = input('Введите набор чисел разделённых пробелами:\n')
print(number_list, file=my_file)
my_file.close()
my_file = open("text5.txt", "r")
list_lines = my_file.read()
my_file.close()
i = 0
sum_n = 0
while i < len(list_lines.split()):
    sum_n += int(list_lines.split()[i])
    i += 1
print(f'Сумма чисел в файле равна: {sum_n}.')

