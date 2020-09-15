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
    room_type = int(request.GET.get("room_types", 0))
    price = int(request.GET.get("price", 0))
    guests = int(request.GET.get("guests", 0))
    bedrooms = int(request.GET.get("bedrooms", 0))
    beds = int(request.GET.get("beds", 0))
    baths = int(request.GET.get("baths", 0))
    s_amenities = request.GET.getlist("amenities")  # array로 받음.
    s_facilities = request.GET.getlist("facilities")  # array 로 받음.
    instant = bool(request.GET.get("instant", False))
    superhost = bool(request.GET.get("superhost", False))
    form = {  # form에서 오는 값
        "city": city,
        "s_room_type": room_type,
        "s_country": country,
        "price": price,
        "guests": guests,
        "bedrooms": bedrooms,
        "beds": beds,
        "baths": baths,
        "s_amenities": s_amenities,
        "s_facilities": s_facilities,
        "instant": instant,
        "superhost": superhost,
    }

    room_types = models.RoomType.objects.all()
    amenities = models.Amenity.objects.all()  # 디비에서 리스트를 뽑아올 값
    facilities = models.Facility.objects.all()  # 디비에서 리스트를 뽑아올 값

    choices = {  # db에서 오는 값
        "countries": countries,
        "room_types": room_types,
        "amenities": amenities,
        "facilities": facilities,
    }

    filter_args = {}

    # Model field 검색하는거임!! filter_args[""]

    if city != "Anywhere":
        filter_args["city__startswith"] = city

    filter_args["country"] = country  # 같은 나라 필터

    if room_types != 0:
        filter_args["room_type__pk"] = room_type  # room_type은 FK이다.

    if price != 0:
        filter_args["price__lte"] = price

    if guests != 0:
        filter_args["guests__gte"] = guests

    if bedrooms != 0:
        filter_args["bedrooms__gte"] = bedrooms

    if beds != 0:
        filter_args["beds__gte"] = beds

    if baths != 0:
        filter_args["baths__gte"] = baths

    if instant is True:
        filter_args["instant_book"] = True

    if superhost is True:
        filter_args["host__superhost"] = True  # FK 사용 시 host fk 부르고 __ 후 해당 값 참조 가능

    if len(s_amenities) > 0:
        for s_amenitiy in s_amenities:
            filter_args["amenities__pk"] = int(s_amenitiy)

    if len(s_facilities) > 0:
        for s_facility in s_facilities:
            filter_args["facility__pk"] = int(s_facility)

    rooms = models.Room.objects.filter(**filter_args)  # 배열 값 빼오기
    return render(request, "rooms/search.html", {**form, **choices, "rooms": rooms})


#  page_kwarg = "potato"  # page 이름

