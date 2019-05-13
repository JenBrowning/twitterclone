from django.urls import path
from twitterclone.authentication.views import (login_view)



urlspatterns = [
    path('login/', login_view)
]