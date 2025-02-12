from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as logouts
from django.shortcuts import render, redirect
from .forms import ReviewForm

def login_view(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home_view')
            else:
                form.add_error(None, "Invalid credentials")
    else:
        form = ReviewForm()

    return render(request, "login/login.html", {"form": form})

def logout_view(request):
     logouts(request)
     return redirect('login')
