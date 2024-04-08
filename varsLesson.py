# Variable = container for value. Behaves as value it contains.

#string
first_name = 'Ben'
last_name = 'Chiasson'
## birthday = (07, 06, 2000)

print((first_name + ' ' + last_name))
print(type(first_name))

#int
age = 23
age += 1 # or age = age + 1
print(age)
print(type(age))
print('Your age is: ' + str(age))

#float
height = 250.5
print('Your height is: ' + str(height) + 'cm')
print(type(height))

#bool
human = True
print('Human? ' + str(human))
print(type(human))