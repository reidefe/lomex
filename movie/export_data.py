import pandas as pd
from load_data import con

dt_actors = pd.read_sql_query("SELECT * FROM actors", con)
dt_movies = pd.read_sql_query("SELECT * FROM movies", con)
dt_writers = pd.read_sql_query("SELECT * FROM writers", con)
print(dt_actors)
