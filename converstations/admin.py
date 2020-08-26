from django.contrib import admin
from .models import Message, Converstation

# Register your models here.


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = (
        "__str__",
        "created",
    )


@admin.register(Converstation)
class ConverStationAdmin(admin.ModelAdmin):
    list_display = (
        "__str__",
        "count_message",
        "count_participants",
    )
