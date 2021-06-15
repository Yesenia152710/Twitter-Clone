from django.db import models
from django.db.models.deletion import CASCADE
from django.utils import timezone
from twitteruser.models import Uzer

# Create your models here.


class Tweets(models.Model):
    tweet = models.TextField(max_length=140)
    user = models.ForeignKey(Uzer, on_delete=CASCADE)
    time_posted = models.DateTimeField(default=timezone.now)
