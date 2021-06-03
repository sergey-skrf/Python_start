import os
import sys
import json
import reguests

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