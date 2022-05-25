# Команды if

cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

print('\nПроверка равенства\n')

car = 'bmw'
print(car == 'bmw')

car = 'audi'
print(car == 'bmw')

print('\nПроверка равенства без учета регистра\n')

car = 'Audi'
print(car == 'audi')
print(car.lower() == 'audi')
print(car)
