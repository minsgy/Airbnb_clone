from django.contrib import admin
from .models import Message, Converstation

# Register your models here.


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    pass


@admin.register(Converstation)
class ConverStationAdmin(admin.ModelAdmin):
    pass
