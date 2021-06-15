"""twitterclone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from twitteruser.views import index_view, profile_view, following_view
from authentication.views import login_view, logout_view, signup_view
from notification.views import notif_view
from tweet.views import tweet_view, tweet_detail
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('tweet/<int:tweet_id>/', tweet_detail),
    path('notification/<int:user_id>/', notif_view),
    path('follow/<int:user_id>/', following_view),
    path('profile/<int:user_id>/', profile_view),
    path('tweets/', tweet_view),
    path('signup/', signup_view),
    path('logout/', logout_view),
    path('login/', login_view),
    path('', index_view, name='home'),
    path('admin/', admin.site.urls),
]
