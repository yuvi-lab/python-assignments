# Assignment 2
# Aim: Perform set operations in Python

# Creating two sets of programming languages
frontend = {"HTML", "CSS", "JavaScript", "React"}
backend = {"Python", "Java", "JavaScript", "NodeJS"}

print("Frontend Technologies:", frontend)
print("Backend Technologies:", backend)

# Union
all_technologies = frontend.union(backend)
print("Union:", all_technologies)

# Intersection
common_technologies = frontend.intersection(backend)
print("Intersection:", common_technologies)

# Difference
only_frontend = frontend.difference(backend)
print("Difference (Frontend only):", only_frontend)
