from django.contrib import admin
from django.urls import path
from django.conf import settings  # media 참조를 위한
from django.conf.urls.static import static
from . import views

app_name = "room"

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
]
