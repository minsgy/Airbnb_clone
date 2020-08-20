from django.db import models

# 모든 나라 fields 값 가져오기
from django_countries.fields import CountryField

# models 라는 name이 같으면 안되므로, as를 이용해 이름 변경
from core import models as core_models
from users import models as user_models

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
    instant_book = models.BooleanField(default=False)  # 바로 예약가능 여부

    # Host field - User
    host = models.ForeignKey(user_models.User, on_delete=models.CASCADE)  # 외래키 연결
