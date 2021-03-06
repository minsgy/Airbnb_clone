from django.db import models

from django.urls import reverse

# 모든 나라 fields 값 가져오기
from django_countries.fields import CountryField

# models 라는 name이 같으면 안되므로, as를 이용해 이름 변경
from core import models as core_models


# 모델들의 공통점으로 들어가는 field 값들을 저장. 이름, 내용, 소제목 등 (item 값들)
class AbstractItem(core_models.TimeStempedModel):
    """Abstract Item"""

    name = models.CharField(max_length=80)  # 이름

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


# hoter room, private room, shared room 등등..
class RoomType(AbstractItem):
    # 각 Room은 여러가지 RoomType을 가질 수 있다. ManyToManyField (N:M)
    """ RoomType Model Definition  """

    class Meta:
        verbose_name = "Room Type"  # verbose_name의 경우 접미사를 두되, 문법에 맞게 대문자 조절이 자동
        # ordering = ["-name"] 순서 정하기 가능


#
class Amenity(AbstractItem):
    """ AmenityType Model Definition  """

    class Meta:
        verbose_name_plural = "Amenties"  # 설정하지 않으면, Class이름에 +s 접미사가 붙음. ex) Amenitys


class Facility(AbstractItem):
    """ Facility Model Definition  """

    class Meta:
        verbose_name_plural = "Facilities"


class HouseRule(AbstractItem):
    """ HouseRule Model Definition"""

    class Meta:
        verbose_name = "House Rule"  # verbose_name의 경우 접미사를 두되, 문법에 맞게 대문자 조절이 자동


class Photo(core_models.TimeStempedModel):
    """ Photo model Definition """

    caption = models.CharField(max_length=80)
    file = models.ImageField(upload_to="room_photos")
    room = models.ForeignKey("Room", related_name="photos", on_delete=models.CASCADE)

    def __str__(self):
        return self.caption


# Create your models here.
class Room(core_models.TimeStempedModel):

    """ Room Model Difinition """

    name = models.CharField(max_length=140)  # 필수요소 - 이름
    description = models.TextField()  # 필수요소 - 상세설명
    country = CountryField()  # country 패키지를 다운
    city = models.CharField(max_length=80)  # 필수요소 - 도시
    price = models.IntegerField()  # 필수요소 - 가격
    address = models.CharField(max_length=140)  # 필수요소

    # room의 요소
    guests = models.IntegerField()
    beds = models.IntegerField()
    bedrooms = models.IntegerField()
    baths = models.IntegerField()
    check_in = models.TimeField()  # 2pm.. 3pm.. 체크인시간 date필드랑 다름
    check_out = models.TimeField()  # 체크아웃
    instant_book = models.BooleanField(default=False)  # 바로 예약 가능 여부

    # Host field - User
    host = models.ForeignKey(
        "users.User", related_name="rooms", on_delete=models.CASCADE
    )
    # 외래키 연결, on_delete는 외래키에만 적용됨. 1:N
    room_type = models.ForeignKey(
        RoomType, blank=True, on_delete=models.SET_NULL, related_name="rooms", null=True
    )
    # 1:N 관계, 한 사람이 하나의 객실 유형을 선택하게 함.
    amenities = models.ManyToManyField("Amenity", related_name="rooms", blank=True)
    facilities = models.ManyToManyField("Facility", related_name="rooms", blank=True)
    house_rules = models.ManyToManyField("HouseRule", related_name="rooms", blank=True)

    def __str__(self):
        return self.name

    # Django model을 저장 할 때 부르는 함수, admin 뿐만 아니라 어디서든
    def save(self, *args, **kwargs):
        self.city = str.capitalize(self.city)  # 첫문자를 대문자로 바꿈.
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("rooms:detail", kwargs={"pk": self.pk})

    def total_rating(self):
        all_reviews = self.reviews.all()
        all_ratings = 0

        if len(all_reviews) > 0:
            for review in all_reviews:
                all_ratings += review.rating_average()
            return round(all_ratings / len(all_reviews))  # 소수점 반올림
        return 0
