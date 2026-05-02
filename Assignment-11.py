

def file_operations():
    filename = "sample.txt"

    # Writing to file
    with open(filename, "w") as file:
        file.write("Hello, this is a sample file.\n")
        file.write("Python file handling is easy.\n")

    print("Data written successfully.\n")

    # Reading file
    with open(filename, "r") as file:
        print("Reading file content:")
        print(file.read())

    # Appending to file
    with open(filename, "a") as file:
        file.write("This line is appended.\n")

    print("\nAfter appending:\n")

    # Reading again
    with open(filename, "r") as file:
        print(file.read())


file_operations()
