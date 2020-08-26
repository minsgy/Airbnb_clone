from django.contrib import admin
from .models import Reservation

# Register your models here.


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):

    list_display = (
        "room",
        "guest",
        "status",
        "check_in",
        "check_out",
        "in_progress",
        "is_finished",
    )

    list_filter = ("status",)
