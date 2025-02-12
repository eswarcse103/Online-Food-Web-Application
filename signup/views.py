from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import login
from .forms import SignupForm

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home_view')
    else:
        form = SignupForm()
    
    return render(request, "signup/signup.html", {"form": form})

def home_view(request):
    return render(request, 'home/index.html')
