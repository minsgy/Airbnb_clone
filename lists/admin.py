from django.contrib import admin
from .models import List

# Register your models here.


@admin.register(List)
class ListAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "user",
        "count_rooms",
    )

    search_fields = ("name",)
    filter_horizontal = ("rooms",)
