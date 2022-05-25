print('4.1 Пицца: создайте список из 3 пицц\n')

pizzas = ['caesar', 'pronto', 'homemade']
for pizza in pizzas:
    print(pizza.title())

pizzas = ['caesar', 'pronto', 'homemade']
for pizza in pizzas:
    print(f'I like {pizza.title()} pizza')

print('\nI really love pizza!')

print('\n4.2 Животные: создайте список из 3 животных\n')

animals = ['dog', 'cat', 'hamster']
for animal in animals:
    # print(animal.title())
    print(f'A {animal.title()} would make a great pet')

print('\nAny of these would make a great pet!')

print('\n4.3 Считаем до 20: создайте список от 1 до 20\n')

numbers = []
for number in range(1,21):
    numbers.append(number)

print(numbers)

print('\n4.4 Миллион: создайте список от 1 до 1000000\n')

numbers = [number for number in range(1, 1000001)]
print(numbers)

print('\n4.5 Суммирование миллиона чисел: воспользуйтесь функциями min, max, sum\n')

print(min(numbers))
print(max(numbers))
print(sum(numbers))

print('\n4.6 Нечетные числа: создайте список от 1 до 20 и отобразите нечетные числа\n')

odd_numbers = [number for number in range(1, 21, 2)]
print(odd_numbers)

print('\n4.7 Тройка: создайте список от 3 до 30, отобразите числа кратные 3\n')

three = [value for value in range(3, 31, 3)]
print(three)

print('\n4.8 Кубы: создайте список и выведите кубы от 1 до 10\n')

cube = [value**3 for value in range(1, 11)]
print(cube)

print('\n4.9 Генератор кубов: из предыдущего задания создать генератор кубов\n')

cube = []
for value in range(1, 11):
    cube.append(value**3)

print(cube)

print('\n4.10 Сегменты: добавьте фрагмент к примерам из файла for_loop or slice\n')

players = ['charles', 'martina', 'michael', 'florence', 'eli']

print('The first three items in the list are:')
print(players[:3])

print('\nThree items from the middle of the list are:')
print(players[1:4])

print('\nThe last three items in the list are:')
print(players[-3:])

print('\n4.11 Моя пицца, твоя пицца: скопируйте упр. 4.1 и добавьте по 1 пицце в каждый список\n')

pizzas = ['caesar', 'pronto', 'homemade']
friend_pizzas = pizzas[:]

pizzas.append('pepperoni')
friend_pizzas.append('meat')

print('My favorite pizzas are:')
for pizza in pizzas:
    print(pizza.title())

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza.title())

print('\n4.12 Больше циклов: из файла foods.py напишите два цикла\n')

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

for food in my_foods:
    print(food.title())

for food in friend_foods:
    print(food)

print('\n4.13 Шведский стол: создайте кортеж из 5 блюд\n')

print('\nThe restaurant, buffet menu')
dishes = ('potatoes', 'caesar', 'meat', 'compote', 'pie')
for dishe in dishes:
    print(dishe.title())

print('\nThe restaurant changed two dishes')
dishes = ('potatoes', 'caesar', 'meat', 'tea', 'cake')
for dishe in dishes:
    print(dishe.title())