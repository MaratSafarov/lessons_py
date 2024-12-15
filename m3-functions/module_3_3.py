def print_params(a=1, b='строка', c=True):
    print(a, b, c)

# 1 - По умолчанию
# print_params()
# print_params('замена А')
# print_params(a='замена А', c='замена С')
# print_params(b=25)
# print_params(c=[1, 2, 3])

# 2 - Распаковка
# values_list = [None, 7, 'текст']
# values_dict = {'a': 1, 'b': 'строка', 'c': True}

# print_params(*values_list)
# print_params(**values_dict)

# 3 - Распаковка + отдельные параметры
values_list_2 = [54.32, 'Строка']

print_params(*values_list_2, 42)
