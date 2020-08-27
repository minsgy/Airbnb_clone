from django.db import models
from django.contrib.auth.models import AbstractUser  # User 모델 커스텀을 위한 참조

# Create your models here.
class User(AbstractUser):

    """ User Model """

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    # (db에 저장되는 값, admin 및 form에 나타낼 값)
    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other"),
    )

    LANGUAGE_ENGLISH = "en"
    LANGUAGE_KOREAN = "kr"

    LANGUAGE_CHOICES = (
        (LANGUAGE_ENGLISH, "en"),
        (LANGUAGE_KOREAN, "kr"),
    )

    CURRENCY_USD = "usd"
    CURRENCY_KRW = "krw"

    CURRENCY_CHOICES = ((CURRENCY_USD, "USD"), (CURRENCY_KRW, "KRW"))

    avatar = models.ImageField(upload_to="avatars", blank=True)  # 사진
    gender = models.CharField(
        choices=GENDER_CHOICES, max_length=10, blank=True
    )  # 성별 - choices="이중튜플이 들어가야함."
    bio = models.TextField(blank=True)
    birthdate = models.DateField(blank=True, null=True)  # date 값만 보여줌.
    # DateTimeField() 시계처럼 보여줄 수 있음.
    language = models.CharField(  # 사용 언어
        choices=LANGUAGE_CHOICES, max_length=2, blank=True
    )

    currency = models.CharField(  # 사용하는 돈 종류
        choices=CURRENCY_CHOICES, max_length=3, blank=True
    )

    superhost = models.BooleanField(default=False)  # 체크박스로 나오게된다.
