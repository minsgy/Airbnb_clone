from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.http import Http404
from . import models


class HomeView(ListView):

    model = models.Room
    paginate_by = 7
    #  paginate_orphans = 5
    ordering = "created"  #
    context_object_name = "rooms"  # 객체를 부르는 이름을 변경


class RoomDetail(DetailView):  # 미친 개쉽다;; 리스트값 전부 반환..
    model = models.Room


#  page_kwarg = "potato"  # page 이름

