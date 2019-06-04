from django.shortcuts import render, reverse, HttpResponseRedirect
from twitterclone.tweet.models import Tweet
from twitterclone.tweet.forms import TweetForm
from django.contrib.auth.decorators import login_required
from twitterclone.notification.models import Notification
from twitterclone.twitteruser.models import TwitterUser
import re



class TweetCreationView(View):
    """Renders a tweet"""
    model = Tweet
    form_class = TweetForm
    url_redirect = "home"
    template_name = "generic.html"
    header = "Create a tweet Girl"
    button_value = "Post Your Tweet"

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name,
        {"header": self.header, "form": form,
        "button_value": self.button_value})


    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            tweet = Tweet.objects.create(
                user=request.user.twitteruser,
                tweet=data["tweet"],
            )
            user_matches = re.findall(r"@(\w+)", data["tweet"])
            for match in user_matches:
                Notification.objects.create(
                    username=TwitterUser.objects.filter(username=match).first(),
                    tweet=tweet
                )
            return HttpResponseRedirect(reverse(self.url_redirect))
        #  else:
        #     form = TweetForm()
            return render(request, self.template_name,
                        {"header": self.header,
                        "form": form, "button_value": self.button_value}


class TweetView(View):
    """Creates a tweet"""

    def get(self, request):
        html = "tweets.html"
        tweets = Tweet.objects.filter(id=id)
        return render(request, html, {"tweets": tweets})

