# Квадраты

squares = []
for value in range(1, 11):
    # square = value**2
    # squares.append(square)
    squares.append(value**2)

print(squares)

print('\nПростая статистика с числовыми списками\n')

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))

print('\nГенераторы списков\n')

squares = [value**2 for value in range(1, 11)]
print(squares)