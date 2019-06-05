import csv

with open("imdb_title_new.csv") as new_csv_file:
    csvcontents = csv.reader(new_csv_file, delimiter=",")
    contents = list(csvcontents)

    with open("imdb_title.csv") as old_csv_file:
        oldcontents = csv.reader(old_csv_file, delimiter=",")
        first_contents = list(oldcontents)

    # for row in contents[1:]:
    #     print(row[3])

    for row in first_contents[1:]:

        try:
            int(row[4])
            int(row[6])
        except ValueError:
            print(row[4],row[6])