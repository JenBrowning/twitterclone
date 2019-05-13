from django import forms

class NewUser(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.Charfield(widget=forms.PasswordInput)
    email = forms.Charfield(widget=forms.EmailInput)


class Login(forms.Form):
    username = forms.Charfield(max_length=30)
    password = forms.Charfield(widget=forms.PasswordInput)
