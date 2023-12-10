# Split a string into a list of words
sentence = "The quick brown fox jumped over the lazy dog"
words = sentence.split()
print(words)

# Output: 
# ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']



# Split a string into a list of words based on a specific delimiter
date = "2022-03-18"
parts = date.split("-")
print(parts)
print()
# Output: ['2022', '03', '18']

# Remember how to do the above - 
# to save the 'parts' into separate variables in one line?
year, month, day = date.split("-")
print(year)    # 2022
print(month)   # 03
print(day)     # 18
print() 


# Split a string into a list of characters using the list CASTING function
word =  "hello"
characters = list(word)
print(characters)
