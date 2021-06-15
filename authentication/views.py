from django.shortcuts import redirect, render, HttpResponseRedirect, reverse
from twitteruser.models import Uzer
from authentication.forms import LoginForm, SignUpForm
from django.contrib.auth import login, logout, authenticate

# Create your views here.


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = Uzer.objects.create_user(username=data['username'],
                                            password=data['password'],
                                            email=data['email'],
                                            first_name=data['first_name'],
                                            last_name=data['last_name'])
            user.save()
            return HttpResponseRedirect(reverse('home'))
    form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                username=data['username'], password=data['password'])
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))
    form = LoginForm()
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    log = logout(request)
    return redirect('home')
