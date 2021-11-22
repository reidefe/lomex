from typing import Dict, List, Mapping
from django.db.models.aggregates import Count
from django.http.response import Http404, HttpResponse
from django.shortcuts import render
from rest_framework import views
from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
)
from rest_framework.response import Response
from .permisions import IsOwnerProfileOrReadOnly
from .serializers import MovieSerializer, ActorSerializer, WrtierSerializer
from .models import WriterModel, ActorModel, MovieModel
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import View, APIView
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)  # noqa
from rest_framework import status
from django.db.models import Avg, Max
from django.http import JsonResponse


class WriterViewSet(ModelViewSet):
    serializer_class = WrtierSerializer
    queryset = WriterModel.objects.all()
    # permission_classes = (IsAuthenticatedOrReadOnly,)


class ActorViewSet(ModelViewSet):
    serializer_class = ActorSerializer
    queryset = ActorModel.objects.all()


class MovieViewSet(ModelViewSet):
    serializer_class = MovieSerializer
    queryset = MovieModel.objects.all()


class GenreViews(APIView):
    """
    Genre services
    """

    def get(self, request, **kwargs):
        data1 = []
        genre = []
        for g in MovieModel.objects.all().distinct():
            a = g.genre
            genre.append(a)

        count_queries = []
        for t in genre:
            c = MovieModel.objects.filter(genre=t).count()
            count_queries.append(c)

        average_queries = []
        for avg in genre:
            v = MovieModel.objects.filter(genre=avg).aggregate(Avg("imdb_rating"))
            average_queries.append(v)

        if average_queries and genre and count_queries:

            for indx in range(len(genre)):
                data2 = {}
                data2["genre"] = genre[indx]
                data2["average"] = average_queries[indx]
                data2["count"] = count_queries[indx]
                data1.append(data2)
            return Response({"genre_details": data1})
        return Http404


class ActorViews(APIView):
    """Actor services"""

    # get all actors and return actors details, movies acted in, and best genre ratings overall
    def get(self, request, **kwargs):

        actor_data = []

        actor_ids = []
        for actor in ActorModel.objects.all()[:20]:
            a = actor.id
            actor_ids.append(a)

        actor_names = []
        for i in actor_ids:
            names = ActorModel.objects.filter(id=i).values_list("name")
            actor_names.append(names)

        movie_query = []
        for m in actor_ids:
            act = MovieModel.objects.filter(actors=m).values_list("title")
            movie_query.append(act)

        genre_query = []
        for g in actor_ids:
            act = MovieModel.objects.filter(actors=g).aggregate(Max("imdb_rating"))
            genre_query.append(act)

        if movie_query:
            for d in range(len(actor_ids)):
                data = {}
                data["name"] = actor_names[d]
                data["movies in"] = movie_query[d]
                data["best genre ratings"] = genre_query[d]
                actor_data.append(data)

            return Response({"actor_details": actor_data})
        return Http404


class DirectorViews(APIView):
    """Director service """

    # get directors details including name, top 3 highest rated movie and top favourite actor that has acted in most movie of said director
    def get(self, request, **kwargs):
        director_data = []
        director_name = []
        for m in MovieModel.objects.all()[:20]:
            if m.director != "N/A":
                director_name.append(m.director)

        best_movie_query = []
        for d in director_name:
            movies = (
                MovieModel.objects.filter(director=d)
                .order_by("-imdb_rating")
                .values("imdb_rating", "title")[:3]
            )
            best_movie_query.append(movies)

        fav_actor_query = []
        for da in director_name:
            fav = {}
            act_id = (
                MovieModel.objects.filter(director=da)
                .values("actors")
                .annotate(count=Count("actors"))
                .order_by("-count")[:3]
            )
            act_name = [
                ActorModel.objects.filter(id=q["actors"]).values("name") for q in act_id
            ]
            fav["actor name"] = act_name
            fav["movie count"] = [act_["count"] for act_ in act_id]
            fav_actor_query.append(fav)

        if director_name:
            for d in range(len(director_name)):
                data = {}
                data["name"] = director_name[d]
                data["best movie"] = best_movie_query[d]
                data["favourite actor "] = fav_actor_query[d]
                director_data.append(data)

            return Response(
                {
                    "director details": director_data,
                }
            )
        return Http404
