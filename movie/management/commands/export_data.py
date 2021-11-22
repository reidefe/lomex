import pandas as pd
import sqlite3
import pandas as pd

con = sqlite3.connect("db.sqlite")


dt_actors = pd.read_sql_query("SELECT * FROM actors", con)
dt_movies = pd.read_sql_query("SELECT * FROM movies", con)
dt_writers = pd.read_sql_query("SELECT * FROM writers", con)
dt_movie_actors = pd.read_sql_query("SELECT * FROM movie_actors", con)
