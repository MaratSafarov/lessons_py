for elem in range(3, 21):
    result = f'{elem} - '
    for x in range(1, elem):
        for y in range(x + 1, elem):
            if elem % (x + y) == 0:
                result += f'{x}{y}'
    print(result)