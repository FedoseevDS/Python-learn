# Использование переменных в строках

first_name = 'ada'
last_name = 'lovelace'
full_name = f'{first_name} {last_name}'

print(full_name)
print(f'Hello, {full_name.title()}!')

message = f'\nHello, {full_name.title()}!'
print(message)

# Табуляция и разрывы строк

print('\nPython')
print('\tPython')
print('Languages:\nPtyhon\nC\nJavaScript\n')

print('Languages:\n\tPython\n\tC\n\tJavaScript\n')

favorite_language = 'python '
print(favorite_language)
favorite_language.rstrip()
print(favorite_language)

favorite_language = '\npython '
favorite_language = favorite_language.rstrip()
print(favorite_language)

favorite_language = ' python '
favorite_language.rstrip() # убирает пропуск с правой стороны
favorite_language.lstrip() # убирает пропуск с левой стороны
favorite_language.strip() # убирает пропуск с обеих сторон


