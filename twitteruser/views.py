from abc import abstractproperty
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render, reverse
from django.contrib.auth.decorators import login_required
from tweet.models import Tweets
from twitteruser.models import Uzer

# Create your views here.


@login_required
def index_view(request):
    userids = []
    mytweets = []
    for user in request.user.following.all():
        userids.append(user.id)
        mytweets.append(request.user.id)
    tweets = Tweets.objects.filter(
        user_id__in=userids).order_by('-time_posted')
    mtweets = Tweets.objects.filter(
        user=request.user.id).order_by('-time_posted')
    return render(request, 'index.html', {'tweets': tweets, 'my': mtweets})


def profile_view(request, user_id):
    who = Uzer.objects.get(id=user_id)
    tweets = Tweets.objects.filter(user=who)
    following = Uzer.objects.filter(pk=1)
    for follow in following:
        following_count = follow.following.all()
    return render(request, 'profile.html', {'tweet': tweets, 'who': who, 'following': following_count})


@login_required
def following_view(request, user_id):
    user = Uzer.objects.get(id=user_id)
    current_user = Uzer.objects.get(id=request.user.id)
    is_following = False
    if user != current_user:
        if user in current_user.following.filter(id=user.id):
            current_user.following.remove(user)
            is_following = False
        else:
            current_user.following.add(user)
            is_following = True
        print(current_user.following.all())
        return redirect('home')

    return HttpResponseRedirect(reverse('home'))
