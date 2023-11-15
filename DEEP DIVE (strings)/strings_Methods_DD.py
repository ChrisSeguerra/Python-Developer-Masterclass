
# USEFUL String Methods Deep Dive

string = "hello"   # Note: Methods do not modify the string in place 
                   # They return a new string. A new memory block and make a new string inside the RAM
string1 = "    world    "
x = string1.rstrip()

lit = "Thy Word is a lamp unto my feet."

start = "Welcome to Python Masterclass!"

string_num = "56789"

fruits = ["apple", "banana", "cherry"]

print(string.upper())                     # converts the string to uppercase                              # Output: HELLO
print(string.capitalize())                # converts the first letter of the String to upper case         # Output: Hello
print(string.lower())                     # converts the string to lower case                             # Output: hello
print(string.partition("hello"))          # returns a TUPLE with 3 element                                # Output: ('', 'hello', '')
print(string.replace("hello", "hi"))      # replaces a specified phrase with another specified phrase.    # Output: hi
print(string.find('e'))                   # finds the first occurrence of the specified value             # Output: 1
print("The", x, "is made by God")         # removes any trailing characters                               # Output: The    world is made by God
print(lit.split())                        # split a string into a LIST where each word is a list item     # Output: ['Thy', 'Word', 'is', 'a', 'lamp', 'unto', 'my', 'feet.']
print(start.startswith("Welcome"))        # returns True if the string starts with the specified value,   # Output: True - the string STARTS with the specified value in the pharenthesis
# Otherwise False.
print(string_num.isnumeric())             # returns True if all the characters are numeric (0-9),         # Output: True - all the characters are numeric
# Otherwise False.
print(fruits.index("cherry"))             # returns the position at the first occurrence                  # Output: 2 OR Orange is not in the list
# of the specific value in the pharenthesis

print(dir(string))                        # gives all available methods for the type

# ^ Output: ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']



# *Replace*
string = "I have a cat."
new_string = string.replace("cat", "dog")
print(new_string)                 # Output: I have a dog.


# *Find*
# NOTE: syntax: find(substring, start index, end index)
text = "hello world"
print(text.find("world", 0, 5))   # Output: 6 if where looking directly to the starting index OR -1 if there nothing found in the string
print(text.find("python"))        # Output: -1
print(text.find("o"))             # Output: 4
print(text.find("l", 4))          # Output: 9 # Starting index is 4

print("")

# Methods
string = "hello"
print(string.upper())        # Output: HELLO
print(string.capitalize())   # Output: Hello


# Methods do not modify the string in place 
# - They Return a New String

upper_cased = string.upper()
print(string)                # Output: hello
print(upper_cased)           # Output: HELLO
