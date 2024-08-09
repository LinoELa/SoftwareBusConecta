from django.shortcuts import render

# 6 B 
from django.shortcuts import redirect
from django.contrib.auth import login , authenticate
from django.contrib import messages


# Create your views here.
# 3 C
def home(request):
    return render (request, 'home.html', {})


# 5 A 
def inicio(request):
    return render(request, 'inicio.html', {})


# 6 C
def login_user(request):
    # 6 E
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        # 6 F
        user = authenticate(request, username = username, password = password)

        # 6 G 
        if user is not None: 
            login(request, user)
            messages.success(request, 'Enhorabuena, has iniciado sesión!')

            return redirect ('inicio')
        else: 
            messages.error(request, 'Error al iniciar session. Porfavor intentalo de nuevo')
            #  NO USO EL REDIRECT porque data un error 


    

    #  6 C B - al crar la funcion
    return render(request, 'form_login.html', {})