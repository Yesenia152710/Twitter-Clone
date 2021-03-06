# Generated by Django 3.2.3 on 2021-06-02 21:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('twitteruser', '0003_alter_following_follow'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='following',
            name='count',
        ),
        migrations.AddField(
            model_name='following',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='following',
            name='follow',
            field=models.ManyToManyField(blank=True, related_name='Following', to=settings.AUTH_USER_MODEL),
        ),
    ]
