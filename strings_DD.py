# A string can use single double qoutes:
string1 = "This is a string."
string2 = 'This is also a string.'


# A string can be one or multiple words:
string1 = "Hello"
string2 = "Hello world"


# Strings are IMMUTABLE:
# message = 'Hello friends'
# message[0] = 'u'
# print(message) #error because Strings are IMMUTABLE


# Multiline strings:
mesg = """
Hello guys, welcome to my channel!
   Hope you have fun thank you :)
                           - Chris
"""
print(mesg)


# Strings Lenghts:
slogan = 'Keep on programming!'
print(len(slogan)) # Output should be 20


# Indexing:
string = "Python"
print(string[0]) # Output: P
print(string[2]) # Output: t


# Negative Indexing:
string = "Python"
print(string[-1]) # Output: n
print(string[-3]) # Output: h


# Slicing:
string = "Funzies"
print(string[2:6]) # Output: nize

# syntax: [from index : to index (but not including!)]

print(string[2:]) # Output: nzies
print(string[:3]) # Output: Fun


# Slicing with step:
string = "123456789"
print(string[1:8:2]) # Output: 2468
# syntax: [from index : to index (but not including!) : step]


# Reverse String:
string = 'hello'
print(string[::-1]) # Output: olleh


# Slicing from the end:
string ="123456789"
print(string[-4:-1]) # Output: 678


# Slicing with variable:
string = 'hello'
start_index = 1
end_index = 4
print(string[start_index:end_index]) # Output: ell


# Concatenation
string1 = "Hello"
string2 = "world"
string3 = string1+" "+string2
print(string3)  # Output: Hello world

# OR example below
#print(string1," ",string2)

