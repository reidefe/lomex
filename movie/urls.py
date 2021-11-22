from django.conf.urls import url
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework import routers
from .views import (
    MovieViewSet,
    ActorViewSet,
    WriterViewSet,
    ActorViews,
    DirectorViews,
    GenreViews,
)

router = routers.SimpleRouter()
router.register(
    r"movies",
    MovieViewSet,
)
router.register(r"actors", ActorViewSet)
router.register(
    r"writer",
    WriterViewSet,
)

urlpatterns = [
    path("api/genres/", GenreViews.as_view(), name="genres"),
    # path("api/genres/<int:pk>", GenreViews().get_specific, name="genres"),
    path("api/actors", ActorViews.as_view(), name="actors"),
    path("api/directors/", DirectorViews.as_view(), name="directors"),
]
urlpatterns += router.urls
