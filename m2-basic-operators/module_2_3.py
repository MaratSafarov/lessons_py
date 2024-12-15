my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
index = 0
while index < len(my_list):
    my_int = my_list[index]
    if my_int < 0:
        break
    index += 1
    print(my_int)
