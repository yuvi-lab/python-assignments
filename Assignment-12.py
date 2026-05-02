# Assignment 12: Count rows in CSV file

import csv

def count_rows(filename):
    count = 0
    with open(filename, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            count += 1
    return count


file_name = "data.csv"
print("Total number of rows:", count_rows(file_name))
