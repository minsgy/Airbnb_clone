from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, View
from django.http import Http404
from django_countries import countries
from django.core.paginator import Paginator
from . import models, forms


class HomeView(ListView):

    model = models.Room
    paginate_by = 7
    #  paginate_orphans = 5
    ordering = "created"  #
    context_object_name = "rooms"  # 객체를 부르는 이름을 변경


class RoomDetail(DetailView):  # 미친 개쉽다;; 리스트값 전부 반환..
    model = models.Room


# class SearchView(View):
#     def get(self, request):
#         country = request.GET.get("country")
#         if country:

#             form = forms.SearchForm(request.GET)
#             if form.is_valid():


def search(request):
    country = request.GET.get("country")

    if country:  # contry에 값을 입력하고 search 했을 때
        form = forms.SearchForm(request.GET)
        if form.is_valid():
            # form으로부터 입력 된 값
            city = form.cleaned_data.get("city")
            country = form.cleaned_data.get("country")
            price = form.cleaned_data.get("price")
            room_type = form.cleaned_data.get("room_type")
            price = form.cleaned_data.get("price")
            guests = form.cleaned_data.get("guests")
            bedrooms = form.cleaned_data.get("bedrooms")
            beds = form.cleaned_data.get("beds")
            baths = form.cleaned_data.get("baths")
            instant_book = form.cleaned_data.get("instant_book")
            superhost = form.cleaned_data.get("superhost")
            amenities = form.cleaned_data.get("amenities")
            facilities = form.cleaned_data.get("facilities")

            filter_args = {}

            if city != "Anywhere":
                filter_args["city__startswith"] = city

            filter_args["country"] = country

            if room_type is not None:
                filter_args["room_type"] = room_type

            if price is not None:
                filter_args["price__lte"] = price

            if guests is not None:
                filter_args["guests__gte"] = guests

            if bedrooms is not None:
                filter_args["bedrooms__gte"] = bedrooms

            if beds is not None:
                filter_args["beds__gte"] = beds

            if baths is not None:
                filter_args["baths__gte"] = baths

            if instant_book is True:
                filter_args["instant_book"] = True

            if superhost is True:
                filter_args["host__superhost"] = True

            for amenity in amenities:
                filter_args["amenities"] = amenity

            for facility in facilities:
                filter_args["facilities"] = facility
            qs = models.Room.objects.filter(**filter_args).order_by("-created")
            paginator = Paginator(qs, 10, orphans=5)
            page = request.GET.get("page", 1)

            rooms = paginator.get_page(page)
            return render(request, "rooms/search.html", {"form": form, "rooms": rooms})
    else:  # 처음 페이지를 켰을 때
        form = forms.SearchForm()

    return render(request, "rooms/search.html", {"form": form})


#  page_kwarg = "potato"  # page 이름

