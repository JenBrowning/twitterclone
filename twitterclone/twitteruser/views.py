from django.shortcuts import render, reverse, HttpResponseRedirect
from twitterclone.twitteruser.forms import SignupForm
from django.contrib.auth import login
from django.contrib.auth.models import User
from twitterclone.twitteruser.models import TwitterUser
from twitterclone.tweet.models import Tweet


def signup_view(request):
    html = "generic.html"
    header = "Signup"
    form = None
    button_value = "Please sign up."
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.create_user(
                username=data["username"], password=data["password"])
            login(request, user)
            TwitterUser.objects.create(
                username=data["username"],
                display_name=data["display_name"],
                user=user
            )
            return HttpResponseRedirect(reverse("home"))
    else:
        form = SignupForm()
    return render(request, html, {"header": header, "form": form,
                                  "button_value": button_value})


def profile_view(request, username):
    html = "twitteruser.html"
    targeteduser = TwitterUser.objects.filter(username=username).first()
    targeteduser_tweets = Tweet.objects.filter(
        user=targeteduser).order_by("-date")
    num_tweets = len(targeteduser_tweets)
    return render(request, html, {"targeteduser": targeteduser,
                                  "tweets": targeteduser_tweets,
                                  "num_tweets": num_tweets})








