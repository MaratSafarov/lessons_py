immutable_var = (1, 2, 'Kazan', 'Urban')
print(immutable_var)
# immutable_var[1] = 5
# immutable_var[3] = 'Moscow'
# print(immutable_var)
# Элементы не изменяются, т.к. кортеж не содержит изменяемые элементы

mutable_list = ([1, 2, 'Kazan', 'Urban'])
mutable_list[1] = 5
mutable_list[3] = 'Moscow'
mutable_list.append('new_data')
print(mutable_list)