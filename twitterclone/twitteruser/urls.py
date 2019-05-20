from django.urls import path
from twitterclone.twitteruser.views import (signup_view, profile_view)

urlpatterns = [
    path("signup/", signup_view),
    path("<str:username>/", profile_view)
]
