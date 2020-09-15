from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.http import Http404
from django_countries import countries
from . import models


class HomeView(ListView):

    model = models.Room
    paginate_by = 7
    #  paginate_orphans = 5
    ordering = "created"  #
    context_object_name = "rooms"  # 객체를 부르는 이름을 변경


class RoomDetail(DetailView):  # 미친 개쉽다;; 리스트값 전부 반환..
    model = models.Room


def search(request):
    city = request.GET.get("city", "Anywhere")
    city = str.capitalize(city)
    country = request.GET.get("country", "KR")
    room_type = int(request.GET.get("room_types", "0"))
    room_types = models.RoomType.objects.all()

    form = {  # form에서 오는 값
        "city": city,
        "s_room_type": room_type,
        "s_country": country,
    }

    choices = {  # db에서 오는 값
        "countries": countries,
        "room_types": room_types,
    }

    return render(request, "rooms/search.html", {**form, **choices})


#  page_kwarg = "potato"  # page 이름

