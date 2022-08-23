from django.contrib.auth.models import User
from django.db import models
from datetime import datetime
import random


def UniqueGenerator(length=3):
    source = "123456789"
    result = ""
    for _ in range(length):
        result += source[random.randint(0, length)]
    return result


class log(models.Model):
    # T : Presence & F: Leave
    id = models.IntegerField(primary_key=True,default=UniqueGenerator)
    type = models.BooleanField(null=True)
    time_stamp = models.DateTimeField(null=True)
    date_created = models.DateTimeField(default=datetime.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # T : Started & F: Ended
    is_started = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.type} {self.user.username} {self.is_started} {self.time_stamp}'

