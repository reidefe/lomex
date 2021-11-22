from django.db import models
from django.db.models import fields  # noqa
from django.db.models.base import Model  # noqa
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User  # noqa
from .rating_enum import MovieRating
from django.contrib.postgres.fields import ArrayField


class ActorModel(models.Model):
    name = models.CharField(verbose_name=_("Имя актера"), max_length=250, blank=True, null=True)

    def __str__(self):
        return self.name


class WriterModel(models.Model):
    name = models.CharField(verbose_name=_("name of  writer"), max_length=250, blank=False)

    def __str__(self):
        return self.name


class MovieModel(models.Model):
    title = models.CharField(verbose_name=_("movie title"), max_length=500)
    decsription = models.TextField(
        verbose_name=_("movie plot"), max_length=500000, null=True, blank=True
    )
    imdb_rating = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        verbose_name=_("movie rating"),
        null=True,
        blank=True,
    )
    genre = models.TextField(
        verbose_name=_("movie genre"), max_length=10000, null=True, blank=True
    )
    director = models.CharField(
        verbose_name=_("Имя актера"),
        max_length=2500,
        blank=False,
        null=True,
    )
    writers = models.ManyToManyField(
        WriterModel,
        verbose_name=_("writers relationship"),
        max_length=25000,
    )
    writers_names = ArrayField(
        models.CharField(verbose_name=_("array of writers names"), max_length=25000),
        null=True,
        blank=True,
    )
    actors = models.ManyToManyField(
        ActorModel, verbose_name=_("actors relationship"), max_length=25000
    )
    actors_names = ArrayField(
        models.CharField(
            verbose_name=_("array of actors names"),
            max_length=25000,
            null=True,
            blank=True, 
        ), null= True, blank=True
    )
    updated_on = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
