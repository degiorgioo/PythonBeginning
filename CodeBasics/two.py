names = ['davide', 'raffi', 'chris']

for name in names:
    print(name)

print(names)

for value in range(1, 5):
    print(value)

numbers = list(range(0, 10))

squares = []
for number in numbers:
    print(number)
    square = number ** 2
    squares.append(square)

print(numbers)
print(squares)

print(sum(squares))
print(min(squares))
print(max(squares))

squares2 = [value ** 2 for value in range(0, 10)]
print(squares2)

squares3 = squares2[:]

squares2[0] = 99

print(squares3)

print(squares2)