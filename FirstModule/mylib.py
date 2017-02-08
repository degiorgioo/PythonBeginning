def mymap(listtoiterate, function):
    for index, entry in enumerate(listtoiterate):
        listtoiterate[index] = function(entry)


def square(number):
    return number * number


def decrement(number):
    return number - 1


def readfile(filepath):
    with open(filepath) as file_object:
        content = file_object.read()
        return content


def calculate(number1, number2, operation):
    result = 0
    try:

        if operation == '*':
            result = number1 * number2
        if operation == '-':
            result = number1 - number2
        if operation == '/':
            result = number1 / number2
        if operation == '+':
            result = number1 + number2

    except ZeroDivisionError:
        # print("You can't divide by zero, amigo!")
        return "__error__"
        # pass -> failing silently

    else:
        return result
