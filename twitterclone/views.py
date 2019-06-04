from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from twitterclone.tweet.models import Tweet
from twitterclone.twitteruser.models import TwitterUser
from django.views import View
from django.utils.decorators import method_decorator



@method_decorator(login_required, name="dispatch")
class HomeView(View):

    def get(self, request):
        html = "home.html"
        current_user = TwitterUser.objects.get(user=request.user)
        tweets_of_user = Tweet.objects.filter(user=request.user.twitteruser)
        followers = current_user.following.all()
        tweets_of_followings = Tweet.objects.filter(user__in=followers)
        tweets = (tweets_of_followings | tweets_of_user).distinct().order_by("-date")
        return render(request, html, {"tweets": tweets})


