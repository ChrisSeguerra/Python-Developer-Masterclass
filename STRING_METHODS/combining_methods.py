
date = "19/07/1998"
first_slash_index = date.find("/")
second_slash_index = date.find("/", first_slash_index)
year = date[second_slash_index + 1:]

millennium = date[second_slash_index + 1] + "000"  

print(year)
print(millennium)



student_id_number = "2021/120/123"
# student_year = student_id_number.find("/")
print(student_id_number[0:4]) # Output: 2021

# section_student_code = student_id_number.find("/", student_year + 1)
print(student_id_number[5:8]) # Output: 120

#student_number = student_id_number[section_student_code + 1:]
print(student_id_number[9:12]) # Output: 123


# String Formatting
name = "John"
age =  30
print("My name is {0} and I am {1} years old.".format(name, age))

print(f"My name is {name} and I am {age} years old.") 
# Output: My name is John and I am 30 years old.
# Same output but different format


int = 100
print(dir(int))