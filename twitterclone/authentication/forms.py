from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput())


class SignUpForm(forms.Form):
    username = forms.CharField(max_length=50)
    display_name = forms.CharField(max_length=500)
    bio = forms.CharField(widget=forms.Textarea(attrs={"rows":"3"}))
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())