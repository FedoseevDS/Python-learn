# 3.1 Имена

names = ['pavel', 'ivan', 'sasha']
print(names[0].title())
print(names[1].title())
print(names[-1].title())

# 3.2 Сообщения

for l in names:
    print(f'I know a man named {l.title()}.')

# 3.3 Собственный список

cars = ['bmw', 'audi', 'lada', 'hunday', 'kia']
for c in cars:
    print(f'I want to buy {c}')

print('\n3.4 Список гостей. Создайте список, включающий минимум трех людей. Затем используйте этот список для вывода сообщения\n')

friends = ['pavel', 'sasha', 'anton']
for f in friends:
    print(f'I invite my friend {f.title()} to lunch')

print('\n3.5 Изменение списка гостей: добавить имя гостя, который придти не сможет, измените список и замените имя гостя\n')

friends = ['pavel', 'sasha', 'anton']
print(f"My friend {friends[-1]} won't be able to come to lunch")
friends.insert(2, 'ivan')
del friends[-1]
for f in friends:
    print(f'I invite my friend {f.title()} to lunch')

print(friends)

print('\n3.6 Больше гостей. Добавьте еще 3 гостей с помощью команды insert and append\n')

print('I bought a large table, so I can invite 3 more guests')
friends.insert(0, 'sveta')
friends.insert(2, 'kate')
friends.append('natasha')
for f in friends:
    print(f'I invite my friend {f.title()} to lunch')

print(friends)

print('\n3.7 Сокращение списка гостей: оставьте только двух гостей\n')

print('Unfortunately lunch is canceled')
print(f"I'm sorry that I won't be able to invite my friend {friends.pop().title()} to lunch")
print(friends)
print(f"I'm sorry that I won't be able to invite my friend {friends.pop().title()} to lunch")
print(friends)
print(f"I'm sorry that I won't be able to invite my friend {friends.pop().title()} to lunch")
print(friends)
print(f"I'm sorry that I won't be able to invite my friend {friends.pop().title()} to lunch")
print(friends)
print(f'{friends[0].title()} the invitation to lunch remains valid')
print(f'{friends[1].title()} the invitation to lunch remains valid')
del friends[0]
print(friends)
del friends[0]
print(friends)

print('\n3.8 Повидать мир: создайте список из 5 стран, используйте методы sorted, reverse, sort\n')

countries = ['china', 'usa', 'germany', 'france', 'egypt']
print(countries)
print(sorted(countries))
print(countries)
print(sorted(countries, reverse=True))
print(countries)
countries.reverse()
print(countries)
countries.reverse()
print(countries)
countries.sort()
print(countries)
countries.sort(reverse=True)
print(countries)

print('\n3.9 Количество гостей: из упражнения с 3.4 по 3.7 выведите количество гостей приглашенных на ланч\n')

friends = ['pavel', 'sasha', 'anton']
print(len(friends))

friends = ['pavel', 'sasha', 'ivan']
print(len(friends))

friends = ['sveta', 'pavel', 'kate', 'sasha', 'ivan', 'natasha']
print(len(friends))

print('\n3.10 Все функции: создайте свой список и воспользуйтесь всеми функциями из прошедших упражнений\n')

cities = ['moscow', 'washington', 'berlin', 'beijing', 'paris', 'kiev']
print(cities[3].title())
print(cities[-2].title())
cities[3] = 'ottawa'
print(cities)
cities.append('riyadh')
print(cities)
cities.insert(0, 'minsk')
print(cities)
del cities[-1]
print(cities)
cities.pop(-3)
print(cities)
cities.remove('washington')
print(cities)
print(sorted(cities))
cities.sort(reverse=True)
print(cities)
cities.reverse()
print(cities)
print(len(cities))