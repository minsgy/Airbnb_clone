from django.contrib import admin
from .models import Room, RoomType, Amenity, Facility, HouseRule, Photo

# Register your models here.
@admin.register(RoomType, Amenity, Facility, HouseRule)
class ItemAdmin(admin.ModelAdmin):
   
    """ Item Model """
    pass


# @admin.register(Amenity)
# class ItemAdmin(admin.ModelAdmin):
#     pass


# @admin.register(Facility)
# class ItemAdmin(admin.ModelAdmin):
#     pass


# @admin.register(HouseRule)
# class ItemAdmin(admin.ModelAdmin):
#     pass


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):


    pass


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    """Photo model definition"""
    pass