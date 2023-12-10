
# A list is the simplest kind of data structure 
# - a way to store multiple values into a single variable

# a single value in a variable -  not a data structure
greetint = "Hi there"

# multiple values in a single variables -  a data structure
numbers = [1, 2, 3, 4, 5] 
print()


# Creating a list - A list is created in Python by placing items inside [], separated 
# by commas. A list can include values of any data type in Python 
# - including other lists. Another way to create an empty list is by using list().

my_list = [] # empty list
my_list = [1, 2, 3] # list of integers
my_list = ['apple', 'banana', 'cherry'] # list of strings
my_list = [1, 'apple', 3.4] # list of different data types
# this is not common/recommended, but it is possible

# Another way to create an empty list:
my_list = list()

# A list can also be composed of other lists!
my_list = [[1,2], [3,4], [8,4]]
print()


# Access Python List Elements is achieved using [] and an index number 
# - indexing starts from 0
fruits = ['apple', 'banana', 'cherry']

print(fruits[0])     # Output: apple
print(fruits[2])     # Output: cherry
print()


# Negative Indexing in Python can be used to 
# access items from the end of the list
my_list = ['apple', 'banana', 'cherry']

print(my_list[-1]) # Output: cherry
print(my_list[-2]) # Output: banana
print()


# Slicing in Python is used to access a range of items in the list
my_list = ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango']

# Syntax: [start index (inclusive) : end index (exclusive)]
print(my_list[2:5])    # Output: ['cherry', 'orange', 'kiwi']

# Indexing with a step:
# Syntax: [start index (inclusive) : end index (exclusive) : step]
print(my_list[1:5:2])  # Output: ['banana', 'orange']


# Reverse a List
my_list = ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango']
print(my_list[::-1])  # Output: ['mango', 'melon', 'kiwi', 'orange', 'cherry', 'banana', 'apple']
print()


# Chnage List Items - using indexing to replace old vaklues with new ones 
# - lists are mutable (vs strings that are not mutable)
my_list = ['apple', 'banana', 'cherry']
my_list[1] = 'orange'
print(my_list)        # Output: ['apple', 'orange', 'cherry']

# Remove an Item From a List
# With del keyword

languages = ['Python', 'Swift', 'C++', 'C', 'Java', 'Rust', 'R']

del languages[1]  
print(languages)    # Output: ['Python', 'C++', 'C', 'Java', 'Rust', 'R']

del languages[-1]
print(languages)    # Output: ['Python', 'C++', 'C', 'Java', 'Rust']

del languages[0:2]  
print(languages)    # Output: ['C', 'Java', 'Rust']
print()


# With the remove() method
my_list = ['apple', 'banana', 'cherry']
my_list.remove('banana')
print(my_list)   # Output: ['apple', 'cherry']
print()


# Concatenating lists works with the "+" operator
words1 = ['hello', "world"]
words2 = ['goodbye', 'mars']

all_words = words1 + words2

print(all_words)  # Output: ['hello', 'world', 'goodbye', 'mars']
print()

# You can find all list methods available using dir().
lst = [1, 2, 3]
print(dir(lst))
print()


# --COMMON-- Python List Methods

# append() - adds an item on the END of the list
my_list = ['apple', 'banana', 'cherry']
my_list.append('orange')  # this will be added at the end of the list
print(my_list)     # Output: ['apple', 'banana', 'cherry', 'orange']
print()

# extend() - extendst the list with the items from another iterable object
my_list = ['apple', 'banana', 'cherry']
other_list = ['orange', 'kiwi', 'melon']
my_list.extend (other_list)
print(my_list)     # Output: ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon']
print()

# insert() - adds an item at a specific index
my_list = ['apple', 'banana', 'banana']
my_list.insert(1, 'kiwi')   # add an item at index 1
print(my_list)    # Output: ['apple', 'kiwi', 'banana', 'banana']
print()

# remove() - removes the FIRST occurrence of an item in the list
my_list = ['apple', 'banana', 'cherry']
my_list.remove('banana')
print(my_list)    # Output: ['apple', 'cherry']
print()

# pop - removes the item at the specified GIVEN INDEX and returns it
my_list = ['apple', 'banana', 'cherry']
my_list.pop()    # remove the last item
print(my_list)    # Output: ['apple', 'banana']
print()

my_list2 = ['apple', 'banana', 'cherry']
my_list2.pop(0)   # remove the item at INDEX 0
print(my_list2)    # Output: ['banana', 'cherry']
print()

# clear() - removes all items from the list
my_list = ['apple', 'banana', 'cherry']
my_list.clear()
print(my_list)   # Output: []
print()

# index() - returns the index of the first occurrence of an item in the list
my_list = ['apple', 'banana', 'cherry', 'banana']
print(my_list.index('banana'))   # Output: 1
print()

# count()- returns the number of items APPEARS in the list
my_list = ['apple', 'banana', 'cherry', 'banana']
print(my_list.count('banana'))  # Output: 2
print()

# sort() - sorts the lsit in ASCENDING ORDER
my_list = [3, 1, 4, 1, 5, 9, 2, 6]
my_list.sort()
print(my_list)   # Output: [1, 1, 2, 3, 4, 5, 6, 9]
print()

# reverse() - reverses the order of the list
my_list = ['apple', 'banana', 'cherry']
my_list.reverse()
print(my_list)   # Output: ['cherry', 'banana', 'apple']
print()

# copy() - returns a copy of the list
fruits = ['apple', 'banana', 'cherry']
fruits_copy = fruits.copy()
print(fruits_copy)   # Output: ['apple', 'banana', 'cherry']
print()




