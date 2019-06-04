import csv



# Objective of this is to get the data and remove gender and title
# We will then return the transformed data

def transform_details(csv_full_name):
    new_details = []

    with open(csv_full_name) as csvfile:
        csv_details = csv.reader(csvfile, delimiter=",")

        # iterable = iter(csv_details)
        # headers = next(iterable)
        #
        # print(iterable, headers)

        for user in csv_details:
            new_details.append([user[1].capitalize(), user[2].capitalize(), user[4]])

    return new_details

transf_data = transform_details("order_details.csv")

# Creating a function to write our transformed data and write to csv

def write_csv(new_data_list, filename):

# Open new file with the option to write
    newfile = open(filename, "w", newline='')
    with newfile:
        csv_writer = csv.writer(newfile, delimiter=",")
        csv_writer.writerows(new_data_list)


# Take our list of rows of transformed data
# write to that file

write_csv(transf_data, "transformed_details.csv")
