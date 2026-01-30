# Assignment 3
# Aim: Demonstrate tuple operations in Python

# Creating a tuple of cities
cities = ("Delhi", "Mumbai", "Chennai", "Kolkata")

print("Cities Tuple:", cities)

# Accessing elements
print("Second City:", cities[1])
print("Last City:", cities[-1])

# Nested Tuple
student_data = ("Rahul", 19, ("Maths", "Physics", "CS"))
print("Nested Tuple:", student_data)
print("Access Nested Element:", student_data[2][1])

# Repetition
repeat_tuple = ("Python",) * 3
print("Repeated Tuple:", repeat_tuple)

# Concatenation
more_cities = ("Pune", "Jaipur")
combined = cities + more_cities
print("Concatenated Tuple:", combined)

