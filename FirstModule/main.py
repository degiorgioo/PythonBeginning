from FirstModule.mylib import *
# from mylib import *

listtotest = list(range(1, 5))

# mylib.mymap(listtotest, square)

mymap(listtotest, square)

print(listtotest)

print(calculate(1, 0, '/'))

if __name__ == '__main__':
    print("main")
