# all() METHOD - returns True if all keys of the dictionary are True or if the dictionary is empty, otherwise False.
# create a dictionary
my_dict = {'name': '', 'age': None, 'address': ''}

# check if all keys have a value
# Output: True
print(all(my_dict))

# add a key with value of None
my_dict['phone'] = None

# check again if any keys have a value
# Output: False
print(all(my_dict.values()))
print()



# any() METHOD - returns True if any key of the dictionary is True, otherwise False.
# create a dictionary
my_dict = {'name': 'Jack', 'age': 26, 'address': 'Downtown'}

# check if any keys have a value
# Output: True
print(any(my_dict))

# add a key with value of None
my_dict['phone'] = None

# check exsitence of keys
# Output: True 
# 'any' only checks for the existence of keys, 
# not the truthiness of their values.
print(any(my_dict))

# create a dictionary with all values set to False
my_dict2 = {'a': '', 'b': '', 'c': ''}

# check if any keys have a value
# Output: False
print(any(my_dict2.values()))
print()



# len() METHOD - returns the number of key-value pairs in the dictionary.
# create a dictionary
my_dict = {'name': 'Jack', 'age': 26, 'address': 'Downtown'}

# Output: 3
print(len(my_dict))



# sorted() METHOD - returns a list of the KEYS in the dictionary, sorted in ascending order.
# create a dictionary
my_dict = {'name': 'Jack', 'age': 26, 'address': 'Downtown'}

# Output: ['address', 'age', 'name']
print(sorted(my_dict))
print()



# clear() METHOD - removes all key-value pairs from the dictionary.
# create a dictionary
my_dict = {'name': 'Jack', 'age': 26, 'address': 'Downtown'}

# clear the dictionary
my_dict.clear()

# Output = {}
print(my_dict)
print()



# keys() METHOD - returns a list of the keys in the dictionary.
# create a dictionary
my_dict = {'name': 'Jack', 'age': 26, 'address': 'Downtown'}

# Output: dict_keys(['name', 'age', 'address'])
print(my_dict.keys())

# Loop over keys of a dict:
for key in my_dict.keys():
    print(f"One of the detail fields is: {key}")
print()
# Output:
# One of the detail fields is: name
# One of the detail fields is: age
# One of the detail fields is: address



# values() METHOD - returns a list of all the values available in the dictionary.
# create a dictionary
my_dict = {'name': 'Jack', 'age': 26, 'address': 'Downtown'}

# Output: dict_values(['Jack', 26, 'Downtown'])
print(my_dict.values())

# Loop over values of a dict:
for value in my_dict.values():
    print(f'One of the values is: {value}')
    print()
    
# Output:
# One of the values is: Jack
# One of the values is: 26
# One of the values is: Downtown



