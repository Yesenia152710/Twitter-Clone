from django.shortcuts import render, HttpResponseRedirect, reverse
from tweet.models import Tweets
from tweet.forms import TweetForm
from notification.models import Notification
from twitteruser.models import Uzer


# Create your views here.
def tweet_view(request):
    if request.method == 'POST':
        form = TweetForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            tweet = Tweets.objects.create(
                tweet=data['tweet'], user=request.user)
            if '@' in data['tweet']:
                notify_create = Notification.objects.create(
                    sender=Uzer.objects.get(username=request.user),
                    message=data['tweet'])
                notify_user = Notification.notify
                return render(request, 'notif.html', {'notify': notify_user})
            return HttpResponseRedirect(reverse('home'))

    form = TweetForm()
    return render(request, 'tweets.html', {'form': form})


def tweet_detail(request, tweet_id):
    detail = Tweets.objects.get(id=tweet_id)
    return render(request, 'tweetdetail.html', {'detail': detail})
