# 1 - The del keyword:
student_id = {111: "Eric", 112: "Kyle", 113: "Butters"}


print("Initial Dictionary: ", student_id)
# Output:  Initial Dictionary: {111: 'Eric', 112: 'Kyle', 113: 'Butters'}
print(student_id[111])

del student_id[111] # Delete the key-value pair with key 111

print("Updated Dictionary: ", student_id)
# Output: Updated Dictionary: {112: 'Kyle', 113: 'Butters'}



# 2 - The pop() method:
My_Dict = {1: "Beck", 2: "Joe", 3: "Kate", 4: "Love"}
data = My_Dict.pop(1) # Remove the item with key 2 and return its value
print(data) # Output: Beck
print(My_Dict) 
# Output: {2: 'Joe', 3: 'Kate', 4: 'Love'}