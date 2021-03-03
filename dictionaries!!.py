# START
## Keep chugging away bb!

# Dictionary: data type that is unordered and mutable
##Consists of key:value pairs; maps value to associated pair

# Create a dictionary(30:00)
mydict = {"name": "Max", "age": 28, "city": "New York"}
print(mydict)

# Dict method for creation
# mydict2 = dict(name = "Mary", age = 27, city = "Boston")
# print(mydict2)

# Acessing values (31:35)
value = mydict["name"]
print(value)

value = mydict["age"]
print(value)

# Adding or changing values (32:18)
##Dictionaries are mutable!
###Fun note: name was moved to the back of the dictionary?

mydict["email"] = "Max@xyz.com"
print(mydict)

"""
# Deleting a method
###I commented this out so I can keep working without retyping code lol###

del mydict["name"]
print(mydict)

mydict.pop("age")
print(mydict)

mydict.popitem()  #removes the first item??
print(mydict)
"""

# Checking for value
if "name" in mydict:
    print(mydict["name"])

##Try and except method? (35:05)

try:
    print(mydict["name"])
except:
    print("Error")

try:
    print(mydict["lastname"])
except:
    print("Error! That's not in the dictionary silly goose.")

# Iterating through a dictionary (36:00)

# For loops:
for key in mydict:
    print(key)  # prints all keys

for key in mydict.keys():
    print(key)

for value in mydict.values():
    print(value)

for key, value in mydict.items():
    print(key, value)

# Copyign a dictionary
##Be careful!

mydict_copy = mydict
print(mydict_copy)

# Modifying the copy modifies the OG! commented out so the proper code works lol
"""
mydict_copy["email"] = "max@123.com"
print(mydict_copy, mydict)
"""
# Notice, just like lists, this changes the OG as well. This is becuase you're referencing the same point in the memory.

# Making a copy that's independent of your OG:
mydict_copy = mydict.copy()
print(mydict_copy)

mydict_copy["email"] = "max@123.com"
print(mydict_copy, mydict)

# Updating a dictionary (39:15)
my_dict = {"name": "Max", "age": 56, "email": "eww@eww.com"}
my_otherdict = dict(name="Martha", age=102, city="Hotlanta")

my_dict.update(my_otherdict)
print(my_dict)

# This is FASCINATING! All existing key pairs were overwritten; email was NOT becuase it was not an item in my_otherdict

# Possible key types
##Can use any immutable type
###Can even use a tuple???

my_dict = {3: 9, 6: 36, 9: 81}
print(my_dict)

# value = my_dict[0]
# Error! Zero isn't in our list and it's not an index.  Use the actual key to access.

value = my_dict[3]
print(value)  # This will return the value 9!

# Use a tuple as a key
mytuple = (8, 7)
my_dict = {mytuple: 15}

print(my_dict)
# Tuples are possible, but a list would throw an exception
# Lists are mutable and can be changed; so it's not hashable and can't be used as a key
