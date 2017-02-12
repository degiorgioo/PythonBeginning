examples = [(1, 2), (3, 4), (5, 6), (7, 8)]

#
# for tuple in tuples:
#    print tuple
#

for example in examples:
    if example[0] <= 1:
        print(example)
    else:
        print("is bigger")

if 2 and 1:
    print(True)
else:
    print(False)

bool1 = True
bool2 = False
bool3 = not bool1

print(bool3)

if bool1 or bool2:
    print("All Bools are true")
else:
    print("One of the bools is false")

if not bool3:
    print("bool1 is true")

if (1, 3) in examples:
    print("Tuple is in list")
else:
    print("Tuple not in list")

age = 19

if age < 18:
    print("you are minor")
elif age == 18:
    print("your are 18")
else:
    print("you are older man")

pizzas = ['pepperoni', 'salami', 'quattro staggioni', 'quattro formaggi']

if 'pepperoni' in pizzas:
    print("Yes we can order pepperoni")
if 'salami' in pizzas:
    print("Yes we can order salami")


empy_list = list()

# empy_list.append("bla")

if empy_list:
    print("list is not empty")
else:
    print("list is empty")

matrix = [[1, 2], [3, 4], [5, 6]]

print(matrix)

for list in matrix:
    for number in list:
        print(number)
