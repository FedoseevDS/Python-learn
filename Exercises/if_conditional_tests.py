print('5.1 Проверка условий: создать не менее 10 условий\n')

car = 'subaru'
print("1. Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\n2. Is car == 'audi'? I predict False")
print(car == 'audi')

user = 'pavel'
print("\n3. Is user != 'pavel'? I predict False")
print(user != 'pavel')

print("\n4. Is user != 'anton'? I predict True")
print(user != 'anton')

number = 5
print("\n5. Is number > 7? I predict False")
print(number > 7)

print("\n6. Is number < 7?")
print(number < 7)

animals = ['dog', 'cat', 'bear']
animal = 'mouse'
if animal not in animals:
    print(f'\n7. This animal {animal.title()} is not included in the main list')

people = ['man', 'woman', 'kid', 'boy', 'girl']
person = 'girl'
if person in people:
    print('\n8. This species refers to humans')

age = 17
print('\n9. If you are over 18 years old, then you are an adult, check your age:')
if age >= 18:
    print('Are you an adult')
else:
    print('You are still a minor')

print('\n10. The last condition')
age = 18
print(age >= 18)

print('\nБольше условий\n')

print('\nПроверка равентства и неравентсва строк')

city = 'Moscow'
print(city == 'Kiev')
print(city != 'London')

print('\nПроверка с использованием функции lower()')

name = 'Pavel'
print(name == 'pavel')
print(name.lower() == 'pavel')

print('\nЧисловые проверки ==, !=, >, <, >=, <=')

number = 37
print(number == 12)
print(number != 35)
print(number > 23)
print(number < 23)
print(number >= 30)
print(number <= 32)

print('\nПроверка с ключевым словом and и or')

age_1 = 23
age_2 = 43
print(age_1 >= 32 or age_2 <= 12)
print(age_1 >= 22 and age_2 <= 55)

print('\nПроверка вхождения элемента в список')

countries = ['russia', 'germany', 'england', 'shina', 'usa']
county = 'italy'
if county in countries:
    print('True')
else:
    print('False')

print('\nПроверка отсутствия элемента в списке')
countries = ['russia', 'germany', 'england', 'shina', 'usa']
county = 'italy'
if county not in countries:
    print('True')
else:
    print('False')