my_dict = {'Ben': 2000, 'Den': 2001, 'Maks': 2002}
print(my_dict)
print(my_dict.get('Den'))
print(my_dict.get('Rob'))
my_dict.update({'Stiv': 2003, 'Tim': 2004})
print(my_dict.pop('Maks'))
print(my_dict)

my_set = {5, 5, 7, 9, 9, 7, 'run', 3.14, 3.14, 'run'}
print(my_set)
my_set.update({('big', 2)})
my_set.discard(9)
print(my_set)