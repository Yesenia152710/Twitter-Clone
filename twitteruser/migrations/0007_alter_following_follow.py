# Generated by Django 3.2.3 on 2021-06-03 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitteruser', '0006_alter_following_follow'),
    ]

    operations = [
        migrations.AlterField(
            model_name='following',
            name='follow',
            field=models.ManyToManyField(related_name='follow_person', to='twitteruser.Following'),
        ),
    ]