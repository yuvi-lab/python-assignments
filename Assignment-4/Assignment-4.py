# Assignment 4
# Aim: Perform dictionary operations

# Creating a dictionary of employee details
employee = {
    "emp_id": 101,
    "name": "Amit",
    "department": "IT",
    "salary": 50000
}

print("Original Dictionary:", employee)

# Accessing elements
print("Employee Name:", employee["name"])

# Updating dictionary
employee["salary"] = 55000
employee["location"] = "Pune"

print("After Update:", employee)

# Removing element
removed_value = employee.pop("department")
print("Removed Department:", removed_value)

# Merging dictionaries
additional_info = {"experience": "2 Years"}
employee.update(additional_info)

print("Final Dictionary:", employee)

