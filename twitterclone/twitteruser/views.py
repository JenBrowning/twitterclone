from django.shortcuts import reverse, render, HttpResponseRedirect
from django.contrib.auth.models import User



def register(request):
    html = 'signup.html'
    form = None

    if form.is_valid():
        data = form.cleaned_data
        user = User.objects.create_user(
            data['username'],
            data['password'],
            data['email']
        )
        login(request, user)
        return HttpResponseRedirect(reverse('home'))





