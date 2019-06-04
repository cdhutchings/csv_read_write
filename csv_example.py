import csv

# Here we load the .csv

"""
-open file
-read line by line
-separate by commas
"""

# with open("order_details.csv", newline='') as csv_file:
#     csvreader = csv.reader(csv_file, delimiter = ",")
#     print(csvreader)
#
#     for row in csvreader:
#         print(row)
#

# iter() creates an iterable object
# next() goes to the next line

# with open("order_details.csv", newline='') as csv_file:
#     csvreader = csv.reader(csv_file, delimiter=",")
#
#     iterable = iter(csvreader)
#     headers = next(iterable)
#
#     for row in iterable:
#         print(row)
#

# list()

with open("order_details.csv", newline='') as csv_file:
    csvreader = csv.reader(csv_file, delimiter=",")

    for list in list(csvreader):
        print(list)


# Transforming and writing to CSV


