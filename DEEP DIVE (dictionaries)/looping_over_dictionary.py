# create a dictionary
squares = {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}

# 1 - using the index to get the item
for i in squares:
    print('key', i, ', value:', squares[i])
print()
# Output:
# key 1 , value: 1
# key 3 , value: 9
# key 5 , value: 25
# key 7 , value: 49
# key 9 , value: 81



# 2 - using items() to get key and value pairs at the same time
for key, value in squares.items():
    print('key', key, ', value:', value)
print()
# Output:
# key 1 , value: 1
# key 3 , value: 9
# key 5 , value: 25
# key 7 , value: 49
# key 9 , value: 81

