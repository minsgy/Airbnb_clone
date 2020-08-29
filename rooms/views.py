from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from . import models


# Create your views here.
def home(request):
    all_rooms = models.Room.objects.all()
    return render(request, "rooms/home.html", {"all_rooms": all_rooms})
