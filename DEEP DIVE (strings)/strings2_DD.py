# Comparing strings:
string1 = "apple"
string2 = "banana"
print(string1 == string2) # Output: False

string1 = "Apple"
string2 = "banana"
print(string1.lower() < string2.lower())  # Output: True


string1 = "apple"
string2 = "app"
string3 = "le"
print(string1 == (string2 + string3)) # Output: True
print(ord("A")) # Output: 65 according to ASCII specification
print(ord("a")) # Output: 97 according to ASCII specification


# String membership tests:
print('C' in 'Code')         # Output: True
print('c' in 'Code')         # Output: False (case-sensitive!)
print('abc' in 'abfc')       # Output: False
print('mail' not in 'gmail') # Output: False




# Multiple variables on the left side:
date_str = "06/19/2002"
day, month, year = date_str.split("/")

print("")

# dir() gives all available methods for the type:
string ="hello"
print(dir(string))

string = "I have a cat."

print("")

# String Formatting:
name = "John"
age = 30

