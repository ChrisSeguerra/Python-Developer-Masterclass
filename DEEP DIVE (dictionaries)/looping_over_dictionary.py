# create a dictionary
squares = {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}

# 1 - using the index to get the item
for i in squares:
    print('key', i, ', value:', squares[i])
print()


# 2 - ueisng items() to get key and value pairs at the same time
for key, value in squares.items():
    print('key', key, ', value:', value)