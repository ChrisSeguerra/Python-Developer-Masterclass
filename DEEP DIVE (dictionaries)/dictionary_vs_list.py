# sample list of numbers 
numbers = [1, 2, 3, 4, 5]

# access the third element in the list
third_number = numbers[2]

# sample list of names
names = ["John", "Jane", "Bob", "Mary"]

# access the third name in the list
third_name = names[2]



# create a dictionary of addresses
addresses = {
    "John": {"address": "123 Main St", "city": "Anytown", "state": "CA"},
    "Jane": {"address": "456 Oal Ave", "city": "Otherville", "state": "NY"},
    "Bob": {"address": "789 Maple St", "city": "Smallville", "state": "TX"},
    "Mary": {"address": "135 Main St", "city": "Bigcity", "state": "IL"}
}

# access John's address
john_address = addresses["John"] ["address"]
print(john_address)


# Creating  a Dictionary of books
books = {
    "Harry Potter": {"author": "J.K. Rowling", "year": 1997},
    "To Kill a Mockingbird": {"author": "Harper Lee", "year": 1960},
    "The Great Gatsby": {"author": "F. Scott Fitzgerald", "year": 1925}
}
HP_author = books["Harry Potter"] ["author"]
HP_year = books["Harry Potter"] ["year"]
print(f"Author: {HP_author}, Year: {HP_year}")