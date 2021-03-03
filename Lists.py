# START
# Let's learn more Python, babe!#

##1##
# Lists: ordered, mutable, allows duplicates


myList = ["banana", "cherry", "apple"]
print(myList)

myList2 = [5, True, "apple", "grape", "apple"]
# Lists can contain different elements!

# to access an element, refer to index position
item = myList[0]
print(item)


item2 = myList[-1]
print(item2)
# If you attempt to call an index too big, it'll throw an error

# iterating over items in a list (03:49)
for i in myList:
    print(i)
"""
for x in myList:
    print(x)
"""

# checking for item within a list
if "banana" in myList:
    print("Yes, banana is in the list!!")
else:
    print("No!")

# Lists2 (05:23)

# number of elements in a list
len(myList)

# append items
myList.append("lemon")
print(myList)

# inserting an item at a specific position (06:00)
# 1 = index position
myList.insert(1, "blueberry")

# removing items using pop method
# removes the last item in a list
item = myList.pop()
print(item)
print(myList)

###################################################################
# removing a specific element (07:10)
myList.remove("cherry")
# if we specify an item not in the list, we throw a Value error

# using clear method to remove ALL  elements
myList.clear()

# reversing a list
myList.reverse()

# sorting a list into asc order(08:10)
myList.sort()
##note: changes the list PERMENTANTELY; create a new list if you don't want the OG to change

# Create a new list with the same elements(09:25)
##Ex: I want a new list with five zeroes
myList3 = [0] * 5
print(myList3)

# Concatenate two lists with the + operator

newList1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

newList2 = newList1 + myList3
print(newList2)

############################################################
###########################################################

# Slicing (10:23)
##Acessing subparts of the list using the colon

newList1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
a = newList1[1:5]  # start and stop index
print(a)

##will print 1,2,3 and 4
###not specifying a start will start at the begining; not specifying a stop will go allteh way to the end!

# Step Index method (12:04)
# By default, the step is one
b = newList1[
    1::2
]  # This goes from the beginning to the end and takes   every second item
print(b)
##negative step ([1::-1]) will reverse the index


# Copying a list (12:40)

list_org = ["banana", "cherry", "apple"]

list_cpy = list_org

print(list_cpy, list_org)

# What happens if i modify the copy?
list_cpy.append("lemon")
print(list_cpy, list_org)
##This shows that appending lemon to the list copy will ALSO  modify the OG
##This is because the assignment  references the same place in the memory!! (list_cpy=list_org)
##Be VERY careful if you copy a list this way.

# Here's a better way to make a copy:
##This one didn't work?
"""
list_cpy2 = list_org.copy()
print(list_cpy2,list_org)
"""

# one more method
list_cpy3 = list_org[:]
##slices from the beginning to the end and creates a copy


#################################################################
#################################################################
# BONUS ROUND#
# List comprehension: elegant and fast way to create a new list from
## an existing list

z = [1, 2, 3, 4, 5, 6]
y = [i * i for i in z]  # list with z's elements squared

# Syntax: [expression iterator list]
# Don't have to use i; can use x or whatever

print(z)
print(y)