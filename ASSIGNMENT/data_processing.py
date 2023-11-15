# 1
sentence = input("Write a sentence below: \n").upper()    # method of converting to upper case letters

print(sentence)

print("")


# 2
# Prompt the user to enter a paragraph
paragraph = input("Write a paragraph below: \n")

# Split the paragraph into words
words = paragraph.split()

# Count the number of words
word_count = len(words)


# Print the {word_count}
print(f"The total number of words is {word_count}.")

print("")


# 3
# Prompt the user for a string
user_input = input("Please enter a STRING: ")

# Check if all characters in the string are digits
is_all_digits = user_input.isdigit()

# Output true or false based on the result
print(is_all_digits)

print("")


# 4
# Prompt the user for a string
input_string = input("Please enter aonther STRING: ")

# Replace all occurrences of "a" with "o"
replace_string = input_string.replace("a", "o")

# Print the modified string
print(replace_string)

print("")


#5
# Prompt the user for their full name
input_fullname = input("Please enter your full name: ")

# Split the full name into individual names in a LIST array
names = input_fullname.split()

# Extract the initials from each name and join them
initials = ''.join(name[0].upper() for name in names)

# Print the initials
print("Your initials are:", initials)

print("")


#6
# Prompt the user for a string
input_string = input("Please enter a STRING: ")

# Get the length of the input string
string_length = len(input_string)

# Print the length of the string
print(f"The length of your string is {string_length}.")