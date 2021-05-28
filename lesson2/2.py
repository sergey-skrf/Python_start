'''
Задание №2. Для списка реализовать обмен значений соседних элементов, т.е. 
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д. 
При нечетном количестве элементов последний сохранить на своем месте. 
Для заполнения списка элементов необходимо использовать функцию input().
'''

# пользователь задаёт произвольный список элиментов через ','
user_elements = input('Введите произвольный список элементов через запитую:\n')

# разбиваем строку пользователя, разделитем является ','
user_modification = user_elements.split(',')

print(user_modification)
i = 0
# осуществляем проверку на четность/нечетность количества элиментов
if len(user_modification) % 2 == 0:

    # циклом проходим по списку с перестановкой значений соседних элиментов (0 и 1, 2 и 3, и т.д.)
    while i <= len(user_modification) - 2:
        user_modification[i], user_modification[i+1] = user_modification[i+1], user_modification[i]
        i += 2
    print(user_modification)
else:
    # так как список нечетный, удаляем последний элимент списка и передаём его в переменную end_element
    end_element = user_modification.pop()

    # циклом проходим по списку с перестановкой значений соседних элиментов (0 и 1, 2 и 3, и т.д.)
    while i <= len(user_modification) - 2:
        user_modification[i], user_modification[i+1] = user_modification[i+1], user_modification[i]
        i += 2

    # в конец получивщегося списка добавляем элемент ранее присвоенный переменной end_element
    user_modification.append(end_element)
    print(user_modification)



#Вариант преподавателя


user_answer = input('Введите список через запятую:')

user_list = user_answer.split(',')
print(user_list)

idx = 0
while idx < len(user_list[:-1]):
    user_list[idx], user_list[idx+1] = user_list[idx+1], user_list[idx]
    idx += 2
print(user_list)