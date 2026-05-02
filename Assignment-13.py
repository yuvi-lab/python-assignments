# Assignment 13: Convert JSON to CSV

import json
import csv

def json_to_csv(json_file, csv_file):
    with open(json_file, "r") as jf:
        data = json.load(jf)

    # Assuming JSON is a list of dictionaries
    keys = data[0].keys()

    with open(csv_file, "w", newline="") as cf:
        writer = csv.DictWriter(cf, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)

    print("JSON converted to CSV successfully!")


json_to_csv("data.json", "output.csv")
