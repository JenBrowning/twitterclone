from django.urls import path
from twitterclone.tweet.views import (TweetCreationView, TweetView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path("tweet/", login_required(TweetCreationView.as_view()),
         name="tweetcreate"),
    path("tweets/", TweetView),
    path("tweet/<int:id>/", TweetView, name="individual")

]