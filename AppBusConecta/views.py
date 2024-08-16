from django.shortcuts import render

# 6 B 
from django.shortcuts import redirect
from django.contrib.auth import login , authenticate , logout
from django.contrib import messages

# 8 I
from .formularios import FormRegistro

# 10 A 
from .models import historial 

# 13 E 
from .formularios import FormAgregar



# Create your views here.
# 3 C
def home(request):
    return render (request, 'home.html', {})


# 5 A - pk = 10
def inicio(request):
    # 10 B
    modelo_historial = historial.objects.all()

    # 10 C
    return render(request, 'inicio.html', {'modelo':modelo_historial})


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


# 7 B 
def logout_user(request):
    # 7 C
    logout(request)

    messages.success(request, 'Has cerrado session')

    return redirect('home')

# 8 B
def register_user(request):
    
    # 8 J - Despues de crear el formulario de registro 
    #  funcion registro_user envialo a nuestro formulario y haz algo
    if request.method == 'POST':

        formulario_registro = FormRegistro(request.POST)

        if formulario_registro.is_valid():
            formulario_registro.save()

            # Conger la informacion del fomulario para  Autentificacion 
            nombre_ususario = formulario_registro.cleaned_data['username']
            password_usuario = formulario_registro.cleaned_data['password1']

            # Para que se autentifique he inicie sesion directamete 
            usuario = authenticate(username = nombre_ususario , password = password_usuario )

            login(request, usuario)


            messages.success(request, 'Registro con exito!')

            return redirect ('home')
    else:
        formulario_registro = FormRegistro()

        return render(request, 'register.html', {'formulario':formulario_registro})
    

    return render(request, 'register.html', {'formulario':formulario_registro})
    



# 11 A 
def modelos_user(request, pk):

    if request.user.is_authenticated:

        modelos_individuales = historial.objects.get(id=pk)

        return render (request, 'modelos.html', {'modelo_individual':modelos_individuales})
    else:
        messages.error(request, 'Debes iniciar session.')
        return redirect ('inicio')


# 12  B
def borrar_user(request,pk):

    if request.user.is_authenticated:

        borrar = historial.objects.get(id=pk)
        borrar.delete()

        messages.success(request,'Registro eliminado!' )
        return redirect('inicio')
    else:
        messages.error(request, 'Debe iniciar sesión')
        return redirect('home')
    
# 13 B
def agregar_user(request):
    # 13 
    formulario_agregar = FormAgregar(request.POST or None)

    if request.user.is_authenticated:

        if request.method == 'POST':

            if formulario_agregar.is_valid():
                formulario_agregar.save()

                messages.success(request, 'Contenido Agregado')
                return redirect('inicio')
            
        return render (request, 'agregar.html', {'formulario':formulario_agregar}) 
    else:
        messages.error(request, 'Debe iniciar sesión')
        return redirect ('home')



# 14 B 
def actualizar_user(request, pk):


    if request.user.is_authenticated:

        id_modelo = historial.objects.get(id=pk)

                #  {POST} = Si hacen algo , {None} = Si no hacen nada  , {instance} = que aparezca el id a cambiar 
        formulario = FormAgregar(request.POST or None, instance=id_modelo)
        
        if formulario.is_valid():
            formulario.save()

            messages.success(request, 'Contenido Actualizado!')
            return redirect ('inicio')
        
        return render (request, 'actualizar.html', {'actualizar':formulario})
        
    else:
        messages.error(request, 'Debe iniciar sesión')
        return redirect ('home')






    
