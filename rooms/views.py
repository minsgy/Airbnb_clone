from django.shortcuts import render
from django.views.generic import ListView
from . import models


class HomeView(ListView):

    model = models.Room
    paginate_by = 7
    #  paginate_orphans = 5
    ordering = "created"  #
    context_object_name = "rooms"  # 객체를 부르는 이름을 변경


def room_detail(request, pk):

    return render(request, "rooms/detail.html")


#  page_kwarg = "potato"  # page 이름

