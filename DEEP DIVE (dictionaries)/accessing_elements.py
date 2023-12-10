# get vs [] for retrieving elements
my_dict = {'name': 'Jack', 'age': 26}

# [] for retrieving elements
print(my_dict['name'])

# get for retrieving elements
print(my_dict.get('age'))

# Accessing name and age seperately
name = my_dict['name']
age = my_dict['age']
# Accessing na'age'
name, age = my_dict['name'], my_dict['age']

# Printing the result
print(f"Name: {name}, Age: {age}")



# Using Square Brackets ('[]')
my_dict = {'name': 'Jack', 'age': 26}
value = my_dict['name']  # Raises KeyError: 'gender' not in dictionary

# Using 'get' Method
my_dict = {'name': 'Jack', 'age': 26}
value = my_dict.get('name', 'Not specified')  # Returns 'Not specified' if 'gender' is not in dictionary