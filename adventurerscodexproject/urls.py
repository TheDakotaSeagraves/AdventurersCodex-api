from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from adventurerscodexapi.views import (
    CharacterViewSet,
    DndClassViewSet,
    RaceViewSet,
    get_current_user,
    login_user,
    register_user,
)

router = routers.DefaultRouter(trailing_slash=False)
router.register(r"characters", CharacterViewSet, basename="character")
router.register(r"dnd-classes", DndClassViewSet, basename="dnd-class")
router.register(r"races", RaceViewSet, basename="race")


urlpatterns = [
    path("", include(router.urls)),
    path("register", register_user),
    path("login", login_user),
    path("current_user", get_current_user),
]
