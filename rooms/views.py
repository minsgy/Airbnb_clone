from django.views.generic import ListView
from . import models


class HomeView(ListView):

    model = models.Room
    paginate_by = 7
    #  paginate_orphans = 5
    ordering = "created"

#  page_kwarg = "potato"  # page 이름

