# This is a single function that is able to perfom the entire etl operation

import csv

def film_etl(film_csv, filename):

    try:
        with open(film_csv) as raw_file:
            csvcontents = csv.reader(raw_file, delimiter=",")
            contents = list(csvcontents)

        new_list = []

        for row in contents:

            new_list.append([row[0], row[1], row[4], row[6], row[7]])


        filtered_list =[]

        filtered_list.append(["Type", "Title", "Year of Release", "Runtime(mins)", "Genre"])

        for row in new_list[1:]:

            if int(row[2]) >= 2015 and row[0] == "movie" and "Comedy" in row[4]:
                filtered_list.append(row)

        newfile = open(filename, "w", newline="")

        with newfile:
            csv.writer(newfile, delimiter=",").writerows(filtered_list)

    except FileNotFoundError:
        print(f"Not been able to find the file {film_csv}. Are you sure it exists in the path and that you've spelt it "
          f"correctly?")

    except IndexError:
        print(f"The file {film_csv} doesn't seem to be structured in the expected way. Please ensure that you have "
          f"selected the correct file and that it is the file you expect.")


film_etl("imdb_title.csv", "imdb_title_new.csv")


