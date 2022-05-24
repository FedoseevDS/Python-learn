# 2.1 Простое сообщение

message = 'Это очень легкое задание\n'
print(message)

# 2.2 Простые сообщения

message = 'Продолжаю выполнять легкие задания'
print(message)
message = 'Еще один коммит для закрепления материала'
print(message)

# 2,3 Личное сообщение

name = 'pavel'
print(f'\nHello {name.title()}, would you like to learn some Python today\n')

# 2.4 Регистр символов в именах

full_name = 'anTon leSov'
print(full_name)
print(full_name.title()) # первые буквы заглавные
print(full_name.upper()) # привел к верхнему регистру
print(full_name.lower()) # привел к нижнему регистру

# 2.5 Знаменитая цитата

name = 'joseph vissarionovich stalin'
print(f'\n{name.title()} once said,\n"An idea is stronger than a weapon"')

# 2.6 Знаменитая цитата 2

famous_person = name
message = 'once said,\n"An idea is stronger than a weapon"'
print(f'\n{famous_person.title()} {message}')

# 2.7 Удаление пропусков

name = '\n\tivan shuvalov\t'
print(name)
print(name.rstrip()) # удаляет пропуск справа
print(name.lstrip()) # удаляет пропуск слева
print(name.strip()) # удаляет пропуски с двух сторон

# 2.8 Число 8

print(6+2)
print(9-1)
print(16/2)
print(2*4)

# 2.9 Любимое число

number = 27
message = 'Мое любимое число, это день я запомнил на всю жизнь, оно говорит .... вот так, число: '
print(f'{message} {number}')

# 2.10 Добавление комментариев

# День когда я решил создать проекты по Python для Github
date = 23
print(f'Меня зовут Дмитрий, начал работать в Python {date} мая 2022 года')

import this






