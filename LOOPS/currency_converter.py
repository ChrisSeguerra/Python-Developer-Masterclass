# 1st Example:
transaction_aed = [23.45, 67.89, 12.34, 78.90, 54.21]

transactions_usd = []


i = 0 # Iterable variable

while i <= len(transaction_aed) - 1:               # 
    item_usd = transaction_aed[i] * 0.27
    print("Converting value",  transaction_aed[i])
    transactions_usd.append(item_usd)
    i += 1 # Increment to avoid infinite loop loop


for item in transaction_aed:
    item_usd = item * 0.27
    print("Converting value",  item)
    transactions_usd.append(item_usd)

# print(transactions_usd)



# 2nd Example:
# lst = [2, 4, 5, 6]

# for number in lst:
#     if number % 2 == 0:
#         print(number * 2)



# 3rd Example:
# students_data = [
# {'name': 'Alice', 'grades' : [85, 88, 92], 'age': 20},
# {'name': 'Bob', 'grades' : [90, 87, 80, 88], 'age': 21},
# {'name': 'Charlie', 'grades' : [78, 80, 82, 77], 'age': 22}
# ]

# for student in students_data:
#     total_grades = sum(student['grades'])
#     number_of_grades = len(student['grades'])
#     average_grade = total_grades / number_of_grades
#     max_grades = max(student['grades'])

#     # Create a message about the students
#     message = f"{student['name']} is {student['age']} years old. \n"
#     message += f"They have an average score of {average_grade: 2f}. \n"
#     message += f"Here are their grades \n"

#     # Adding a nested loop to iterate over grades and create 
#     for idx, grade in enumerate(student['grades']):
#         message += f"\t Test {idx + 1}: {grade}\n"

#     # Check if the students is graduating (assuming average grade above 85 score)
#     if average_grade >= 85:
#         message += f"{student['name']} is graduating with honors!\n"
#     else:
#         message += f"{student['name']} is graduating.\n"
    
#     # Print message
#     print(message)


