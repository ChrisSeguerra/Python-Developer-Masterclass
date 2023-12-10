
# Create a dictionary with courses and initial students
courses = {
    "math": ["Alice", "Bob", "Charlie", "Diana", "Eve"],
    "hsitory": ["Frank", "Grace", "Henry", "Iris", "John"],
    "chemistry": ["Kevin", "Laura", "Mark", "Nancy", "Oliver"]
    }

# Add 5 students to "math"
random_names = ["Peter", "Quinn", "Rachel", "Sam", "Tom"]
courses["math"].extend(random_names)
# extend() method modifies the existing list in-place
# This means it doesn't create a new list but instead ADDS the new elements to the end of the EXISTING list.

# Remove the third student from "history"
del courses["hsitory"][2]

# Print the students in "chemistry"
print(f"Students in chemistry: {courses['chemistry']}")

# Add a new course "physics" with 4 random students
new_physiscs_students = ["Victor", "Wanda", "Xavier", "Yolanda", "Zoe"], 4
courses["physics"] = new_physiscs_students

# Print all courses and students
for course, students in courses.items(): # Iterates through a dictionary called 'courses' and 
    print(f"{course}: {students}")       # Prints the keys (courses) and their corresponding values (students) in a 'formatted way'.



