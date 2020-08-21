from django.db import models
from core import models as core_models

# Create your models here.


class Converstation(core_models.TimeStempedModel):

    participants = models.ManyToManyField("users.User", blank=True)

    def __str__(self):
        return str(self.created)


class Message(core_models.TimeStempedModel):

    message = models.TextField()

    """ Foreignkey """
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    conversation = models.ForeignKey("Converstation", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} says... {self.message}"
