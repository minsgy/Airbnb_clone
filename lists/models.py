from django.db import models
from core import models as core_models

# Create your models here.


class List(core_models.TimeStempedModel):
    name = models.CharField(max_length=80)

    # 외래키
    user = models.ForeignKey(
        "users.User", related_name="lists", on_delete=models.CASCADE
    )
    rooms = models.ManyToManyField("rooms.Room", related_name="lists", blank=True)

    def __str__(self):
        return self.name

    def count_rooms(self):
        return self.rooms.count()  # 리스트에 있는 Room 객체의 개수

    count_rooms.short_description = "Number of Rooms"
