from django.db import models
from django.db.models.deletion import CASCADE
from django.template.defaultfilters import slugify
from twitteruser.models import Uzer

# Create your models here.


class Notification(models.Model):
    sender = models.ForeignKey(
        Uzer, related_name='sender', on_delete=CASCADE, null=True)
    receiver = models.ForeignKey(
        Uzer, related_name='reciever', on_delete=CASCADE, null=True)
    message = models.TextField()
    read = models.BooleanField(default=False)

    def parse_at(self):
        mentions = [slugify(i)
                    for i in self.message.split() if i.startswith('@')]
        return Uzer.objects.filter(username__in=mentions)

    @property
    def notify(self):
        targets = []
        for user in self.parse_at():
            targets.append(user.id)
        return targets
