from django.shortcuts import render

# from django.http import HttpResponse
from django.core.paginator import Paginator
from . import models


# Create your views here.
def home(request):
    page = request.GET.get("page")
    room_list = models.Room.objects.all()
    paginator = Paginator(room_list, 5, orphans=2)  # 5개씩 끊기
    rooms = paginator.get_page(page)
    return render(request, "rooms/home.html", {"page": rooms})

