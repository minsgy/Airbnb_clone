from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.urls import reverse
from django.http import Http404
from . import models


class HomeView(ListView):

    model = models.Room
    paginate_by = 7
    #  paginate_orphans = 5
    ordering = "created"  #
    context_object_name = "rooms"  # 객체를 부르는 이름을 변경


def room_detail(request, pk):
    try:
        room = models.Room.objects.get(pk=pk)
        return render(request, "rooms/detail.html", {"room": room})
    except models.Room.DoesNotExist:
        raise Http404()


#  page_kwarg = "potato"  # page 이름

