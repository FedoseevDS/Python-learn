print('\nУпорядочение списка\n')

# Постоянная сортировка списка методом sort

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort() # алфавитный порядок
print(cars)

cars.sort(reverse=True) # обратный алфавитный порядок
print(cars)

print('\nВременная сортировка списка функцией sorted()\n')

cars = ['bmw', 'audi', 'toyota', 'subaru']

print('Here is the original list:')
print(cars)

print('\nHere is the sorted list:')
print(sorted(cars))

print('\nReverse order')
print(sorted(cars, reverse=True))

print('\nHere is the original list again:')
print(cars)

print('\nВывод списка в обратном порядке reverse()\n')

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

cars.reverse()
print(cars)

cars.reverse()
print(cars)

print('\nОпределение длины списка\n')

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))

