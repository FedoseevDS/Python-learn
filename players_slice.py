# Создание сегмента

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[2:])
print(players[-3:])

print('\nПеребор содержимого сегмента\n')

players = ['charles', 'martina', 'michael', 'florence', 'eli']

print('Here are the first three players on my team:')
players = [player for player in players[:3]]
print(players)
# for player in players[:3]:
#    print(player.title())

