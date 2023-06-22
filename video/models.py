from django.db import models
from shortuuidfield import ShortUUIDField


class Room(models.Model):
    roomId = ShortUUIDField()

    def __str__(self):
        return self.roomId
