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


class PhotoInline(admin.TabularInline):
    model = Photo


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
    inlines = (PhotoInline,)
    # admin안에 admin 추가. Photo를 Room admin에서 관리가능

    fieldsets = (
        (
            "Basic Info",
            {"fields": ("name", "description", "country", "city", "address", "price")},
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
    raw_id_fields = ("host",)  # 긴 리스트를 위한 필드 출력법
    search_fields = ("=city", "^host__username")
    filter_horizontal = ("amenities", "facilities", "house_rules")

    # admin 패널에서 저장 및 변경 한 값을 반환
    # def save_model(self, request, obj, form, change):
    #     print(obj, change)
    #     super().save_model(request, obj, form, change) super() 반드시 불러야댐

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
