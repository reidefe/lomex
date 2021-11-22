from django.contrib import admin
from .models import MovieModel, ActorModel, WriterModel

admin.site.register(MovieModel)
admin.site.register(WriterModel)
