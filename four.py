children_davide = {
    "child1": {
        'name': "lilly",
        'color': "violet",
        'age': 2
    },
    "child2": {
        'name': "marco",
        'color': "green",
        'age': 4
    }
}

alien_davide = {
    'name': "Davide",
    'color': "blue",
    'age': 18,
    'children': children_davide
}

print(alien_davide['name'])
print(alien_davide['color'])
print(alien_davide['age'])

for child, childInfo in alien_davide['children'].items():
    print(child)
    print(childInfo)

key_values = {
        "Person1": "Sven",
        "Person2": "Matto",
        "Person3": "Davide",
        "Person4": "Chris"
}


print(key_values.keys())
print(key_values.values())

# sorted is only temporary!!!
for key in sorted(key_values):
    print(key)

for value in sorted(key_values.values()):
    print(value)

print(key_values.items())
