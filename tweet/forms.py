from django import forms
from django.db.models import fields
from tweet.models import Tweets


class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweets
        fields = ['tweet']
