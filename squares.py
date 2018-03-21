number = list(range(5,21,5))
print(number)

dice = []
for num in range(1,11):
    dice.append(num**3)
print(dice)


squares = []
for value in range (1,11):
    square = value**2
    squares.append(square)
print(squares)

squares = []
for value in range (1,11):
    squares.append(value**2)

print(squares)

squares = [value**3 for value in range(1,11)]
print(squares)
