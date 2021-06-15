from twitteruser.models import Uzer
from django.shortcuts import render
from notification.models import Notification
from django.contrib.auth.decorators import login_required
from twitteruser.models import Uzer

# Create your views here.


@login_required
def notif_view(request, user_id):
    notify = Notification.objects.all()
    return render(request, 'notif.html', {'notifs': notify})
