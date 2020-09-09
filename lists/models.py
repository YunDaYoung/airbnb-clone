from django.db import models
from core import models as core_models

class List(core_models.TimeStempModel):

    """ List Model definition """

    name = models.CharField(max_length=80)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    room = models.ManyToManyField("rooms.Room", blank=True)

    def __str__(self):
        return self.name

