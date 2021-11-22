import pandas as pd
from .export_data import dt_actors, dt_writers, dt_movies, dt_movie_actors
from django.core.management.base import BaseCommand
from typing import Any, Optional
from sqlalchemy import create_engine
from django.conf import settings
from ...models import MovieModel, ActorModel, WriterModel
from ...models import ActorModel, MovieModel
import base64


class Command(BaseCommand):
    """A command to add data from dataframe into database"""

    help = " A command to add data from dataframe into database"

    def handle(self, *args: Any, **options: Any):

        # Attempt to load the data into the

        # user = settings.DATABASES["default"]["USER"]
        # password = settings.DATABASES['default']['PASSWORD']
        # database_name = settings.DATABASES['default']['NAME']

        # # engine = create_engine('sqlite:///db.sqlite3')
        # database_url = f'postgresql://{user}:{password}@localhost:5432/{database_name}'

        # engine = create_engine(database_url, echo=True)

        # dt_movies.to_sql(MovieModel._meta.db_table, if_exists='replace', con=engine, index=False)
        # dt_actors.to_sql(ActorModel._meta.db_table, if_exists='replace', con=engine, index=False)
        # dt_writers.to_sql(WriterModel._meta.db_table, if_exists='replace', con=engine, index=False)
        # for data, y in dt_actors.iteritems():
        #     actor = ActorModel.objects.create(y)

        for index, row in dt_actors.iterrows():
            model = ActorModel()
            model.name = row["name"]
            model.save()

        for index, row in dt_writers.iterrows():
            model = WriterModel()
            model.name = row["name"]
            model.save()

        for index, row in dt_movies.iterrows():
            model = MovieModel.objects.create(
                title=row["title"], genre=row["genre"], director=row["director"]
            )
            if row["imdb_rating"] != "N/A":
                model.imdb_rating = row["imdb_rating"]
            model.decsription = row["plot"]
            movie_actors = [
                actor["actor_id"]
                for idx, actor in dt_movie_actors.iterrows()
                if row["id"] == actor["movie_id"]
            ]
            for ma in movie_actors:
                if ma:
                    actor_name = ActorModel.objects.get(pk=ma)
                    model.actors_names = [actor_name.name]
                    model.save()
            model.actors.set(movie_actors)
            writer = [
                idx
                for idx, name in dt_writers.iterrows()
                if row["writer"] == name["id"]
                if idx != 0
            ]
            writer_name = [
                name["name"]
                for idx, name in dt_writers.iterrows()
                if row["writers"] == name["id"]
            ]
            # model.writers.set(writer)
            # if writer_name:
            #     for name in writer_name:
            #         query_names = [name.name for name in WriterModel.objects.filter(name=name)]
            #         model.writers_names = query_names
            #         model.save()
            # elif writer:
            #     for x in writer:
            #         wn = WriterModel.objects.filter(id=x)
            #         model.writers_names = wn

            # else:
            #     for x in writer:
            #         model.writers.set(x)

            model.save()
