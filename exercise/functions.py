import csv

# Open and organise the csv file correctly. This will take in the raw csv file and output the headers and body

def open_csv(raw_csv):

    with open(raw_csv) as csv_file:
        csvcont = csv.reader(csv_file, delimiter=",")
        contents = list(csvcont)

        header = contents[0]
        body = contents[1:]
        #print(header)

        return contents

        #print(body)

        # for row in body:
        #     print(row)
        #     pass

# Transform the file as requried

def list_reduce(csv_list):

    new_list = []

    for row in csv_list:

        new_list.append([row[0], row[1], row[4], row[6], row[7]])

    return new_list


def date_filter(reduced_list):

    filtered_list = []

    for row in reduced_list[1:]:

        if int(row[2]) >= 2015 and row[0]=="movie":
            filtered_list.append(row)

    return filtered_list

# Write an updated imdb csv file

def write_film_csv(list, filename):
    newfile = open(filename, "w", newline="")

    with newfile:
        csv.writer(newfile, delimiter=",").writerows(list)


write_film_csv(date_filter(list_reduce(open_csv("imdb_title.csv"))), "imdb_title_new.csv")