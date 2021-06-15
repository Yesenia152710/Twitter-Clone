# Generated by Django 3.2.3 on 2021-06-02 19:15

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitteruser', '0002_following'),
    ]

    operations = [
        migrations.AlterField(
            model_name='following',
            name='follow',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]