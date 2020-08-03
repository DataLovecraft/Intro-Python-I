# For the exercise, look up the methods and functions that are available for use
# with Python lists.
from typing import List

x: List[int] = [1, 2, 3]
y: List[int] = [8, 9, 10]

# For the following, DO NOT USE AN ASSIGNMENT (=).

# Change x so that it is [1, 2, 3, 4]
#print(x.append(4))

x.append(4)
print(x)
assert x == [1, 2, 3, 4]

# Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]

x.extend(y)
print(x)
assert x == [1, 2, 3, 4, 8, 9, 10]

# Change x so that it is [1, 2, 3, 4, 9, 10]

x.remove(8)
print(x)
assert x == [1, 2, 3, 4, 9, 10]

# Change x so that it is [1, 2, 3, 4, 9, 99, 10]

x.insert(5, 99)
print(x)
assert x == [1, 2, 3, 4, 9, 99, 10]

# Print the length of list x

print(len(x))
assert len(x) == 7

# Print all the values in x multiplied by 1000
print([i * 1000 for i in x])
