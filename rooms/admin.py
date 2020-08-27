from django.contrib import admin
from django.utils.html import mark_safe
from .models import Room, RoomType, Amenity, Facility, HouseRule, Photo

# Register your models here.
@admin.register(RoomType, Amenity, Facility, HouseRule)
class ItemAdmin(admin.ModelAdmin):

    """ Item Model """

    list_display = (
        "name",
        "used_by",
    )

    def used_by(self, obj):  # 해당 타입이 포함된 rooms 갯수
        return obj.rooms.count()


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
    fieldsets = (
        (
            "Basic Info",
            {"fields": ("name", "description", "country", "address", "price")},
        ),
        ("Times", {"fields": ("check_in", "check_out", "instant_book")},),
        (
            "More About the Spaces",
            {"fields": ("amenities", "facilities", "house_rules")},
        ),
        ("Spaces", {"fields": ("guests", "beds", "bedrooms", "baths")}),
        ("Last Details", {"fields": ("host",)}),
    )
    list_display = (
        "name",
        "country",
        "city",
        "price",
        "guests",
        "beds",
        "bedrooms",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
        "count_amenities",  # 함수로 제작
        "count_photos",
        "total_rating",  # review의 외래키를 역참조, 출력만 하게함.
    )
    list_filter = (
        "instant_book",
        "room_type",
        "amenities",
        "facilities",
        "house_rules",
        "city",
        "country",
    )

    search_fields = ("=city", "^host__username")
    filter_horizontal = ("amenities", "facilities", "house_rules")

    def count_amenities(self, obj):
        return obj.amenities.count()

    def count_photos(self, obj):
        return obj.photos.count()  # related_name


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    """Photo model definition"""

    list_display = (
        "__str__",
        "get_thumnail",
    )

    # admin register에서 2번째 인수는 해당 클래스 객체 가리킨다.
    # Django Input 무시를 안전하다고 인식 시켜서, HTML에 적용하게 하는 함수 mark_safe()
    def get_thumnail(self, obj):
        return mark_safe(f'<img width="50px" src="{obj.file.url}" />')

    get_thumnail.short_description = "Thumbnail"
