from django.shortcuts import render


# Create your views here.
# 3 C
def home(request):
    return render (request, 'home.html', {})


# 5 A 
def inicio(request):
    return render(request, 'inicio.html', {})
