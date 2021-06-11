import os
import sys
import json
import reguests
from my_pakage.my_pak import my_fun

'''
#1
base_url = 'https://api.github.com/users/'
user_name = sys.argv[1]

url = f'{base_url}{user_name}'
response = reguests.get(url)

file_folder = os.getcwd()
file_path = os.path.join(file_folder, 'some_file.txt')
print(file_path)

with open(file_path, 'r') as file:
	data = file.read()
	print(data)
	print('#'*15)
	j_data = json.loads(data)
	print(j_data)

#print(os.getcwd())


#2

list_comp = [itm for itm in range(10)]
dict_comp = {idx: itm for idx, itm in enumerate(range(10), start=5)}
print(list_comp)
print(dict_comp)


#3
file_folder = os.getcwd()
file_path = os.path.join(file_folder, 'some_file.txt')
print(file_path)

with open(file_path, 'w') as file:
	for key, value in dict_comp.items():
		file.write(f'{key}------{value}\n')


with open(file_path, 'r') as file:
	for line in file:
		prinit(line)

'''
#4 Генераторы
for itm in my_fun(5):
	print(itm)