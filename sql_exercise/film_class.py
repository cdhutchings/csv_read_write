import pyodbc

class SqlConn:

    def __init__(self, server="localhost,1433", database="movies", username="SA", password="Passw0rd2018"):
        self.server = server
        self.database = database
        self.username = username
        self.password = password
        self.docker_con = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL '
                                'Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)
        self.cursor = self.docker_con.cursor()

    def query(self, sql_query):

        return self.cursor.execute(sql_query)


class Film:

    film_instances = []

    def __init__(self, type, primary_title, original_title, is_adult, startyear, endyear, runtime, genre):
        Film.film_instances.append(self)
        self.type = type
        self.title = primary_title
        self.original_title = original_title
        self.is_adult = is_adult
        self.year = startyear
        self.endyear = endyear
        self.runtime = runtime
        self.genre = genre

    def cleanup(self):

       try:
           int(self.year)
       except ValueError:
           self.year = 0

       try:
           int(self.endyear)
       except ValueError:
           self.endyear = 0

       try:
           int(self.runtime)
       except ValueError:
           self.runtime = 0

       if self.genre == r"\N":
           self.genre = ""



