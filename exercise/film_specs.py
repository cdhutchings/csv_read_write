import csv

with open("imdb_title_new.csv") as csv_file:
    csvcontents = csv.reader(csv_file, delimiter=",")
    contents = list(csvcontents)

    def test_date():

        for row in contents[1:]:
            assert row[2] >= 2015
