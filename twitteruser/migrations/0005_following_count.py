# Generated by Django 3.2.3 on 2021-06-02 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitteruser', '0004_auto_20210602_2136'),
    ]

    operations = [
        migrations.AddField(
            model_name='following',
            name='count',
            field=models.IntegerField(default=0),
        ),
    ]