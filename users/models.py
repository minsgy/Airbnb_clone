from django.db import models
from django.contrib.auth.models import AbstractUser

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

    LANGUAGE_ENGLISH = "english"
    LANGUAGE_KOREAN = "korean"

    LANGUAGE_CHOICES = (
        (LANGUAGE_ENGLISH, "en"),
        (LANGUAGE_KOREAN, "kr"),
    )

    CURRENCY_USD = "usd"
    CURRENCY_KRW = "krw"

    CURRENCY_CHOICES = ((CURRENCY_USD, "USD"), (CURRENCY_KRW, "KRW"))

    avatar = models.ImageField(null=True, blank=True)  # 사진
    gender = models.CharField(
        choices=GENDER_CHOICES, max_length=10, null=True, blank=True
    )  # 성별 - choices="이중튜플이 들어가야함."
    bio = models.TextField(null=True, blank=True)
    birthdate = models.DateField(null=True)  # date 값만 보여줌.
    # DateTimeField() 시계처럼 보여줄 수 있음.
    langauge = models.CharField(  # 사용 언어
        choices=LANGUAGE_CHOICES, max_length=2, null=True, blank=True
    )

    currency = models.CharField(  # 사용하는 돈 종류
        choices=CURRENCY_CHOICES, max_length=2, null=True, blank=True
    )

    superhost = models.BooleanField(default=False) # 체크박스로 나오게된다.
