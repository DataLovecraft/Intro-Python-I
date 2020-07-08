"""
List comprehensions are one cool and unique feature of Python.
They essentially act as a terse and concise way of initializing
and populating a list given some expression that specifies how
the list should be populated.

Take a look at https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
for more info regarding list comprehensions.
"""

# Write a list comprehension to produce the array [1, 2, 3, 4, 5]

array = [i for i in range(1, 6)]
print (array)
assert array == [1, 2, 3, 4, 5]

# Write a list comprehension to produce the cubes of the numbers 0-9:
# [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]

cube = [x ** 3 for x in range(10)]
print(cube)
assert cube == [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]

# Write a list comprehension to produce the uppercase version of all the
# elements in array a. Hint: "foo".upper() is "FOO".

a = ["foo", "bar", "baz"]
y = [x.upper() for x in a]
print(y)
assert y == ['FOO', 'BAR', 'BAZ'], "value should be in upper case"

# Use a list comprehension to create a list containing only the _even_ elements
# the user entered into list x.

x: int = input("Enter comma-separated numbers: ").split(',')
y = [int(i) for i in x if int(i) % 2 == 0]
print(y)
