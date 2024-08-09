from django.shortcuts import render


# Create your views here.
# 3 C
def home(request):
    return render (request, 'home.html', {})
