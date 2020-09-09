from django.db import models
from core import models as core_models

class List(core_models.TimeStempModel):

    """ List Model definition """

    name = models.CharField(max_length=80)
    user = models.ForeignKey("users.User", related_name="list", on_delete=models.CASCADE)
    room = models.ManyToManyField("rooms.Room", related_name="list", blank=True)

    def __str__(self):
        return self.name

