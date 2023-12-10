
# Python List Comprehension
# syntax: [(expression) for (name) in (iterable)]
numbers = [number+2 for number in range(1, 5)]
print(numbers)


# this is equivalent to:
numbers = []

for x in range(1, 6):
    numbers.append(x + 2)
print(numbers)
# The first option is more elegant (one line instead of 3) - more 'Pythonic'