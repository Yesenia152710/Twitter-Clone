from django import forms
from twitteruser.models import Uzer


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)


class SignUpForm(forms.ModelForm):
    class Meta:
        model = Uzer
        fields = ['username', 'password', 'first_name', 'last_name', 'email']
