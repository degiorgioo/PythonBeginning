
def saymesomething(something):
    print(something)


def sayhello():
    """Das ist ein Kommentar."""
    print("Hello World")


def callfunction(function):
    function()


def saymetwothings(something_one, something_two):
    print(something_one)
    print(something_two)


def proofequality(obj1, obj2):
    return obj1 == obj2


def optionalparam(obj1, obj2=""):
    print(obj1 + " " + obj2)


def buildcar(brand, name, ps=0):
    car = {"brand": brand, "name": name}
    if ps:
        car['ps'] = ps
    return car


def iteratelist(listtoiterate):
    for entry in listtoiterate:
        print(entry)


def modifylist(listtomodify):
    for index, entry in enumerate(listtomodify):
        listtomodify[index] = 1


def trytomodifylist(listtomodify):
    listcopy = listtomodify[:]
    for index, entry in enumerate(listcopy):
        listcopy[index] = 2


def sumallarguments(*ints):
    result = 0
    for number in ints:
        result += number
    return result


sayhello()
saymesomething("Hallo du geile Sau!!")

callfunction(sayhello)

saymetwothings(something_one="hello", something_two="you")

print(proofequality("hello", "hello"))
print(proofequality(1, 2))

optionalparam("Davide", "De Giorgio")

car1 = buildcar("Ferrari", "F50")
car2 = buildcar("Fiat", "500", 200)

listofcars = list()

listofcars.append(car1)
listofcars.append(car2)

iteratelist(listofcars)

listofints = list(range(1, 5))

modifylist(listofints)

print(listofints)

trytomodifylist(listofints)

print(listofints)

print(sumallarguments(1, 2, 3, 4))

