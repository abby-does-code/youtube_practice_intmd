# START
##Still learning Python, babe!

# Tuple: collection data type that is ordered an immutable;
##similar to a list; main differnece is that a tuple can't be changed.
##Often used for objects that bELONG TOGETHER

##Let's go:##

mytuple = ("Max", 28, "Boston")
print(type(mytuple))
print(mytuple)

# Can use built in tuple function to create a tuple from an iterable
mytuple = tuple(["Max", 28, "Boston"])
print(type(mytuple))

# Accessing elements in a tuple:
item = mytuple[0]  # first item
print(item)
# Throws an index error if you call an index out of range

# Negative index:
item = mytuple[-1]  # Calls the last item in the tuple
print(item)

# Change tuple elements???
# mytuple[0] = "Tim"
# Throws a type error ("does not support assignment") because a tuple is immutable

# Iterate over a tuple
for i in mytuple:
    print(i)

# Check if element is in tuple
if "Max" in mytuple:
    print("Yes it is!")
else:
    print("Nope.")

#
mytuple = ("a", "p", "p", "l", "e")
print(len(mytuple))

# Count elements in a tuple (21:40)
print(mytuple.count("p"))

# Find the first index
print(mytuple.index("p"))

# Convert a tuple to a list
my_list = list(mytuple)
print(type(my_list))

mytuple = tuple(my_list)
print(type(mytuple))

# Slicing (23:48)
# Good way to access subparts of the tuple

a = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# Syntax: item = tuple[index]
b = a[2:5]
print(b)  # index 2, 3, and 4
# same rules as lists - not referencing a start point starts at beginning, etc.

# Step
b = a[::2]
c = a[::-1]  # this reverses

# Unpacking??? (25:48)

newtuple = "Mark", 78, "Baltimore"

name, age, city = newtuple  # Much match number of items in tuple
print(name)
print(age)
print(city)

# unpack multiple elements with a star (26:50)
##not sure why this didn't work; invalid syntax?
###need to check versions
"""
newtuple = (0,1,2,3,4)

i1, *i2, i3 = newtuple #unpack?

print(i1)
print(i3)
print(i2)

#This is supposed to create a list
"""

# Compare a tuple and a list (27:43)
##bc tuple immutable, python can make some optimizations
###Working with a tuple can be easier/more efficient sometimes!

# Ex:

import sys

my_list = [0, 1, 2, "hello", True]  # List
my_tuple = (0, 1, 2, "hello", True)  # Tuple

print(sys.getsizeof(my_list), "bytes")  # Return number of bytes
print(sys.getsizeof(my_tuple), "bytes")

# Output:
# For list: (112, bytes)
# For tuple: (96, bytes)

# List is larger!

# One more example:
import timeit

print(timeit.timeit(stmt="[0,1,2,3]", number=1000000))
print(timeit.timeit(stmt="(0,1,2,3)", number=1000000))

# Output:
# For list: 0.104802131653
# For tuple: 0.0123710632324