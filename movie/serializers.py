from rest_framework import serializers
from .models import ActorModel, MovieModel, WriterModel


class WrtierSerializer(serializers.ModelSerializer):
    class Meta:
        model = WriterModel
        fields = "__all__"


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieModel
        fields = "__all__"


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActorModel
        fields = "__all__"
