
# Iterating through a list using loops
fruits = ['apple', 'banana', 'cherry']
for fruits in fruits:
    print(fruits)
print()

# Output: apple
#		  banana
#		  cherry
           
# We can use loops to also print items more instructively with f strings:
fruits = ['apple', 'banana', 'cherry']
for fruits in fruits:
    print(f"My favorite fruit is {fruits}")
print()
# Output:
	# My favourite fruit is apple
	# My favourite fruit is banana
	# My favourite fruit is cherry


# Check if an item exsists  in the Python List
fruits = ['apple', 'banana', 'cherry']
fruit_to_look_for = 'kiwi'
if fruit_to_look_for in fruits:
	  print(f"Yes, {fruit_to_look_for} is in the fruits list")
else:
	  print(f"No, {fruit_to_look_for} is not on the fruits list")


# List Length
my_list = ['apple', 'banana', 'cherry']
print(len(my_list))         # Output: 3
print()

my_empty_list = []
print(len(my_empty_list))   # Output: 0
print()

