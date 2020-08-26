from django.db import models
from django.utils import timezone  # 현재 시간을 비교하기 위해 import
from core import models as core_models

# Create your models here.


class Reservation(core_models.TimeStempedModel):
    """Reservations Model Definition"""

    STATUS_PENDING = "pending"
    STATUS_CONFIRMED = "confirmed"
    STATUS_CANCLED = "canceled"

    STATUS_CHOICE = (
        (STATUS_PENDING, "Pending"),
        (STATUS_CONFIRMED, "Confirmed"),
        (STATUS_CANCLED, "Canceled"),
    )

    status = models.CharField(
        max_length=12, choices=STATUS_CHOICE, default=STATUS_PENDING
    )
    check_in = models.DateField()  # 날짜
    check_out = models.DateField()  # 날짜

    """ForeignKey"""
    guest = models.ForeignKey("users.User", on_delete=models.CASCADE)
    room = models.ForeignKey("rooms.Room", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.room} - {self.check_in}"

    def in_progress(self): # 방에 사람이 있는가?
        now = timezone.now().date()
        return now > self.check_in and now < self.check_out  # boolean값 출력

    in_progress.boolean = True

    def is_finished(self): # 체크 아웃을 하였는가?
        now = timezone.now().date()
        return now > self.check_out

    is_finished.boolean = True