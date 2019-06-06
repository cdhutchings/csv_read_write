import csv
from film_class import *

connection = SqlConn()

# Opens the csv file and allows python to read each line
try:
    with open("imdb_title_sql.csv", newline='') as csv_file:

        csvreader = csv.reader(csv_file, delimiter=",")

    # For each line, create a film instance using the data

        for rows in list(csvreader)[1:]:

            inst_film = Film(rows[0], rows[1], rows[2], rows[3], rows[4], rows[5], rows[6], rows[7])

            inst_film.cleanup()

            #connection.query("DELETE FROM film_list")

        for item in Film.film_instances:

            # print(f"('{item.type}', '{item.title}', '{item.original_title}', {item.is_adult},"
            #                  f"{item.year}, {item.endyear}, {item.runtime}, '{item.genre}')")


            connection.query(f"INSERT INTO film_list ([type], title, original_title, is_adult, [year], endyear, "
                             f"runtime, genre)"
                             f"VALUES ('{item.type}', '{item.title}', '{item.original_title}', {item.is_adult},"
                             f"{item.year}, {item.endyear}, {item.runtime}, '{item.genre}')")

        #connection.docker_con.commit()

except pyodbc.DataError:
    print("There is an issue with the database. Please ensure your query is written in the correct SQL notation and "
          "that your database is structured to accept the data you are inserting.")

