# Сравнение чисел

answer = 17

if answer != 42:
    print('That is not the correct answer. Please try again!')

age = 19
print(age < 21)
print(age <= 21)
print(age > 21)
print(age >= 21)

print('\nПроверка нескольких условий\n')

# Использование and для проверки нескольких условий

age_0 = 22
age_1 = 18
print(age_0 >= 21 and age_1 >= 21)

age_1 = 22
print(age_0 >= 21 and age_1 >= 21)

print('\nИспользование or для проверки нескольких условий\n')

age_0 = 22
age_1 = 18
print(age_0 >= 21 or age_1 >= 21)

age_0 = 18
print(age_0 >= 21 or age_1 >= 21)

print('\nПроверка вхождения значений в список\n')

requested_toppings = ['mushrooms', 'onions', 'pineapple']
print('mushrooms' in requested_toppings)
print('pepperoni' in requested_toppings)