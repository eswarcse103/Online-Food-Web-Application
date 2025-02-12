from django import forms

class ReviewForm(forms.Form):
    username = forms.CharField(label="Username", max_length=100, error_messages={
        "required": "Please enter your username",
        "max_length": "Your username is too long"
    })
    password = forms.CharField(label="Password", widget=forms.PasswordInput, min_length=8)
