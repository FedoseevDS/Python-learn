# Списки

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

# Обращение к элементам списка

print(bicycles[0])
print(bicycles[0].title())
print(bicycles[1])
print(bicycles[3])
print(bicycles[-1]) # обращаюсь к последнему элементу списка

# Использование отдельных элементов из списка

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
message = f'\nMy first bicycle was a {bicycles[0].title()}.'

print(message)
