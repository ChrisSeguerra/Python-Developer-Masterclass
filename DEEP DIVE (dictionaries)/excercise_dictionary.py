def count_items():  
    item_counts = {}

    while True:                    # This line starts an infinite loop that will continue until the user enters "done".
        item = input("Enter an item (or 'done' to finish): ") # This line prompts the user to enter an item and stores their input in the variable item
        if item == 'done':         # This line checks if the user entered "done".
            break                  # If they did, the break statement is used to exit the loop.

        if item in item_counts:    # This line checks if the item is already exists in the 'item_counts' dictionary.
            item_counts[item] += 1 # If the item exists, this line increments the value associated with that key by 1.
        else:                      # If the item does not exist, this block creates a new key-value pair in the dictionary.
            item_counts[item] = 1  # This line sets the value for the new key (the user's item) to 1, indicating that it has been seen once.
    
    return item_counts             # This line returns the dictionary to the caller.

if __name__ == '__main__':         # It checks if the current module is being run directly as a script (meaning it's the main program) using the __name__ == '__main__' condition.
# If the condition is true, it implies the code inside the block will only be executed if the script is run directly, not when it's imported as a module by another script.
    item_counts = count_items()    # This line calls the count_items() function and assigns its return value (a dictionary containing item counts) to the variable item_counts.

    print("\nItem_counts: ")
    for item, count in item_counts.items():  # This line iterates over the key-value pairs in the 'item_counts' dictionary.
    # The variable 'item' will hold each item name, and the variable 'count' will hold the corresponding number of occurrences.    
        print(f'{item}: {count}')            # This line prints a formatted string where item and count are substituted with their respective values.
        # This will print the item name and its count on separate lines.


# 1. Prompt the user to enter items until they enter "done".
# 2. Keep track of the number of times each item has been entered.
# 3. Print the final count for each item.
# This code demonstrates the use of dictionaries and loops to handle user input and maintain counts for individual items.