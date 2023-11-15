# SYNTAX = round(number, num_digits)

# round to 0 decimal places (same as int())
print (round(3.14))         # Output: 3

# round to 1 decimal place
print (round(3.14159, 1))   # Output: 3.1

# round 2 decimal places
print (round(3.14159, 2))   # Output: 3.14

# round 3 decimal places
print (round(3.14159, 3))   # Output: 3.142


print("")
# Note that the round() function uses "round half to even" 
# (also known as "banker's rounding") when rounding. 
# This means that if the digit to be rounded is exactly 5, 
# the function rounds to the nearest even number. 

# For example:
print (round(2.5))           # Ouput: 2
print (round(3.5))           # Ouput: 4