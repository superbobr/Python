s = tuple(map(int, input().split()))
magic_number = int(input())
start = 0
try:
    i = s.index(magic_number)
except ValueError:
    print(f'Число {magic_number} встречается 0 раз(а) в кортеже.')  
    print(f'Число {magic_number} не найдено в кортеже.')
else:
    k = s.count(magic_number)
    print(f'Число {magic_number} встречается {k} раз(а) в кортеже.')  
    print(f'Первое вхождение числа {magic_number} находится на индексе {i}.')
