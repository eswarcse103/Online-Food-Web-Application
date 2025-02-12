from django.shortcuts import render

# Create your views here.

def thank_you(request):
    return render(request, 'thank_you/thank_you.html')
