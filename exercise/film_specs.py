import csv
import pytest

with open("imdb_title_new.csv") as csv_file:
    csvcontents = csv.reader(csv_file, delimiter=",")
    contents = list(csvcontents)

    def test_date():

        for row in contents[1:]:
            assert int(row[2]) >= 2015

    def test_comedy():

        for row in contents[1:]:
            assert "Comedy" in row[4]

    def test_type():

        for row in contents[1:]:
            assert row[0] == "movie"
