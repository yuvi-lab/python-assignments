# Assignment 1
# Aim: Demonstrate various list operations in Python

# Creating a list of student marks
marks = [78, 85, 62, 90, 74]

print("Original List:", marks)

# Accessing elements
print("First element:", marks[0])
print("Last element:", marks[-1])

# Adding elements
marks.append(88)              # Add at end
marks.insert(2, 80)           # Insert at index 2

print("After Adding Elements:", marks)

# Removing elements
marks.remove(62)              # Remove specific value
marks.pop()                   # Remove last element

print("After Removing Elements:", marks)

# Sorting list
marks.sort()
print("Sorted List (Ascending):", marks)

# Reversing list
marks.reverse()
print("Reversed List:", marks)

# Slicing list
sliced = marks[::-1]
print("Reversed List (Descending):", sliced)
