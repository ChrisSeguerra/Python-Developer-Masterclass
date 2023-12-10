# Create a list of dictionaries 
books = [                                # This line defines a variable named books and assigns it a list of three dictionaries.
    {                                    # Each dictionary within the list represents a book and contains three key-value pairs.
        "title": "Harry Potter and the Sorcerer's Stone",  # The title of the book (string) 
        "author": "J.K. Rowling",                          # The author of the book (string)
        "year": 1997                                       # The year the book was published (integer)
    },
    {
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "year": 1960
    },
    {
        "title": "The Lord of the Rings",
        "author": "J.R,R Tolkien",
        "year": 1954
    }
]

print(books[1]["title"]) # Prints the "title" of the book at index [1]. 
print(books[2]["year"])  # Prints the "year" of the book at index [2]
print()

for books in books:      # This line initiates a loop that iterates over each dictionary within the books list.
    print(f"Title: {books['title']}")   # This line prints the title of the current book using f-strings for "formatted output".
    print(f"Author: {books['author']}") # Similarly, this line prints the author of the current book in a "formatted output".
    print(f"Year: {books['year']}")     # Same as the year.
    print()



# Note: !!!
# ITERATES:
# In plain English, "iterates" means to 'repeat something a number of times, one after another'.
# It's like going through a list of items one by one, or doing a loop in a programming language.
# Define a list of dictionaries to store book information.

# 1. Define a list of dictionaries to store book information.
# 2. Access specific data within a dictionary based on its key and index.
# 3. Loop through a list of dictionaries and access information from each dictionary.
# 4. Use f-strings for formatted output.