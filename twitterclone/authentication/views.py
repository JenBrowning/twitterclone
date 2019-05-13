from django.shortcuts import render, reverse, HttpResponseRedirect
from twango.authentication.forms import LoginForm
from django.contrib.auth import authenticate, login



def login_view(request):
    html = "login.html"
    form = None

    if request.method == 'POST':
        form = Login.(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                username=data['username'],
                password=data['password']
            )
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(request.GET.get('next', '/'))
    else:
        form = Login()
    return render(request, html, {'form': form})