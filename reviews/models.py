from django.db import models
from core import models as core_models

# Create your models here.


class Review(core_models.TimeStempedModel):

    """ Review Model Definition """

    review = models.TextField()  # 리뷰 내용적기

    """ 평점 적기 항목 """
    accuracy = models.IntegerField()
    communication = models.IntegerField()
    cleanliness = models.IntegerField()
    location = models.IntegerField()
    check_in = models.IntegerField()
    value = models.IntegerField()

    """ FoeignKey """
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    room = models.ForeignKey("rooms.Room", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.review} - {self.room}"

