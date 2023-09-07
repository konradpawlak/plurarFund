menus1 = [ 
    ['Egg Sandwich', 'Bagel', 'Coffee',],
    ['BLT', 'PB&J', 'Turkey',],
    ['Soup', 'Taco', 'Burger',],
    ]
print('Breakfast Menu:\t', menus1[0])
print('Lunch Menu:\t', menus1[1])
print('Dinner Menu:\t', menus1[2])

# only bagel
print(menus1[0][1])

# instead of list of lists we can use a dictionary

menus2 = { 'Breakfast': ['Egg Sandwich', 'Bagel', 'Coffee',],
     'Lunch': ['BLT', 'PB&J', 'Turkey',],
     'Dinner': ['Soup', 'Taco', 'Burger',],
}
print(menus2)

print('Breakfast Menu:\t', menus2['Breakfast'])
print('Lunch Menu:\t', menus2['Lunch'])
print('Dinner Menu:\t', menus2['Dinner'])

for key, value in menus2.items():
    print(key + '->' + str(value))

# dict can be used as objects, atributes saved as key and value pairs
person = {
    'name': 'Rreoo',
    'surname': 'Crater',
    'age': 100,
    'city': 'Crynidon',
}

print(person.get('name') + ', the greatest ' + person.get('surname'),'. Living in the ', person.get('city'), ' for the last ', str(person.get('age')) + ' years.')