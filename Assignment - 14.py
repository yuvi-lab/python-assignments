# Assignment 14: File Exception Handling

filename = input("Enter file name: ")

try:
    with open(filename, "r") as file:
        print(file.read())

except FileNotFoundError:
    print("Error: File not found!")

except PermissionError:
    print("Error: Permission denied!")
