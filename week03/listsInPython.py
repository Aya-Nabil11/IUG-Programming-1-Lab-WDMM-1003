# python List
'''
In Python, a list is a built-in data structure
that can hold an ordered collection of items.
Unlike arrays in some languages, Python lists are very flexible:

Creating a List :
1. Using Square Brackets
a = [1, 2, 3, 4, 5] # List of integers
b = ['apple', 'banana', 'cherry'] # List of strings
c = [1, 'hello', 3.14, True] # Mixed data types
2. Using list() Constructor
a = list((1, 2, 3, 'apple', 4.5))
3. Creating List with Repeated Elements
a = [2] * 5
b = [0] * 7

print(a)
print(b)






















Can contain duplicate items
Mutable: items can be modified, replaced, or removed
Ordered: maintains the order in which items are added
Index-based: items are accessed using their position (starting from 0)
Can store mixed data types (integers, strings, booleans, even other lists)
'''
# we use the variables to store one values .
# if we have 15 students we need lists
# names = ["aya" , "ahmed" ,"salem" , "salem"]
# print(type(names))
# print(names)
# access indivdaul element by index
# print(len(names))

# slicing
# [starting index , lenght , steps]
# print(names[-1])
# print(names[0:6])
# names.sort() # sort the original list
# names.reverse()
# print(names)
# print(max(names))
# print(min(names))

# add some data to the list

# names.append("soso")
# print(names)

# insert in specifi place

# names.insert(3,"nana")
# print(names)

# add more thn one item at the end of the list
# names.etend(["sami" , "omar" ,"sameer"])
# names[1]="sami";

# list are mutable we can change the data of the list after we create it
names = ["aya" , "ahmed" ,"salem" , "salem"]
names[0:3]=["aya","sss","qwd"];
print(names)
names.remove("aya")
print(names)















x=5
b=10
print(x%b)