age = input("Please your age: ")

if age <= 18:
    print("You are minor")
else:
    print("You are not minor: " + str(age))

current_tries = 1

"""
while current_tries <= 5:
    number = input("Number: ")
    print(number)
    current_tries += 1

current_tries_two = 1
sentence = ""
while current_tries_two <= 5:
    word = input("Word: ")
    print(word)
    sentence += str(word)
    current_tries_two += 1

print(sentence)

"""