from django.db import models
from core import models as core_models

# Create your models here.


class Converstation(core_models.TimeStempedModel):

    participants = models.ManyToManyField(
        "users.User", related_name="converstations", blank=True
    )

    def __str__(self):
        usernames = []
        for user in self.participants.all():
            usernames.append(user.username)
        return ", ".join(usernames)  # str() 값으로 반환해야함.

    def count_message(self):  # 메세지 개수
        return self.messages.count()

    count_message.short_description = "Number of Message"

    def count_participants(self):  # 채팅 참여 인원
        return self.participants.count()

    count_participants.short_description = "Number of Participants"


class Message(core_models.TimeStempedModel):

    message = models.TextField()

    """ Foreignkey """
    user = models.ForeignKey(
        "users.User", related_name="messages", on_delete=models.CASCADE
    )
    conversation = models.ForeignKey(
        "Converstation", related_name="messages", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.user} says... {self.message}"
