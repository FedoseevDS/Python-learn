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


