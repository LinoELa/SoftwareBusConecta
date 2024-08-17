# SoftwareBusConecta"

#### BASIC 

1. Configuracion basica 
    - proyecto 
    - app 
    - base de datos 

2. Subir a Github 

3. Contruir la apliacion basica 
    - urls 
    - views
    - plantilla (home.html)

4. Contruir la plantilla base 
    - base.html 
    - Probar si funciona 
    - Vincular Bootstrap
    - Crear Carpeta ( STATIC )
    - Construir Carpeta ( CSS ) & Vincular .css - Bootstrap(bootstrap_styles.css)- STATIC
    - Hacer el extends en ( home )
    - 
    - Nombre de Auto 
    - Cargar Archivos estatico ( load static )
    - Favicon
    - Google Fonts
    - 
    - navbar.html
    - Configuramos todo el navbar 


5. Contruimos [Diseño] toda la parte (home) - (inicio)
    - (home) - Layout basico que veran los usuarios NO LOGIN 
    - (inicio) - Layout basico que veran los usuario YES LOGIN
    - 
    - Vista & Plantilla de (Inicio.html)




#### LOGIC DJANGO

6. Iniciar Sesion [ Primera Logica - (LogIn) ]
    - (Views) importamos los modulos a utitilizar : 
        - ( django.shortcuts ) - redirect
        - ( django.contrib.auth ) - log in , log out y autenticacion 
        - ( django.contrib ) - messages
    - url & funcion  login_user   & Plantilla 
    - Plantilla Layout - formuario a rellenar para inciciar sesion
    - Poner que se pueda ver la contraseña 
    - 
    - Implementar [AUTENTIFICACION] 
    - Autentificacion (form_login.html) para que NO SE VEA los ya LOGIN
    - (6 F - G ) configuarar la FUNCTION par que la persona qeu haga el POST de form se verifique 
    - (6 H ) en (base.html) Configurar bucle mensajes de errores 
    - 
    - (6 I ) - Vincular Inicio al (navbar)


7. Cerra Sesion [ Logica - (LogOut) ]
    - Creamos la url 
    - Cramos la funcion que simplemtente con la logica hacer un return a home
    - Cremos el link en navbar 
        - Ponemos lo de autentificacion 
        - en user login ponemos que haya un Cerrar Sesion
    - Configuramos navbar para la vista del el login y el logout

##### HOME - LOGIN - LOGOUT => navbar.html poner lo qeu se tiene que ver por cada estado

8. Registro Usuarios [logica - (register_user) ]
    Es algo un poco asi de complicado
    No son los datos que se guardan en la base de datos , el MODELO es lo que se guarda en la base de datos.
    - Creamos la url 
    - Cramos la funcion con pass 
    - Cremos la plantilla - 
    - Vincular la url al navbar 
    - Creamos el formulario de datos que iran al registro [formularios.py]
        - User: solo puede guardar nombre de usuario y contraseña , si queremos guardar otra cosa 
        tenemos que  extender el modelo User
            - Agregar - AbstractUser al formulario 
            - a [settings.py]AUTH_USER_MODEL = 'tu_app.CustomUser' 


9. Modelo - (BBDD)
    El modelo es para guardar la informacion en la base de datos 
    - Crear el modelo con los datos que queremos guardar 
    - Hacer una migracion a la base de datos 
    - admin - hacer que se vea alli - revisar en admin
    - Mirar la carpeta de migracion que se ha creado en la app 
    - Crear algunos modelos 


10. Modelo (Ver en Pantalla) 
    - Añadimos  ejemplos de modelos desde el admin
    - Intamos traer los modelos a la pantalla principal 
    - Hacer los bucles con lo que hemos guardado en la funcion {'nombre' : variable}
    - Layout - Bootstrap
    - 
    - lINK - VER INDIVUAL 
    - 
11. Modelo ( link : Ver Indivual ) (BASICO)
    - url con pk para poder habr cada modelo 
    - views 
    - plantilla 
    - La funcion : en una variable obtener los objeto por id
    def modelos_user(request, pk):
    - Configurar inicio par aque haya un link para ver de forma individual



```
    if request.user.is_authenticated:

        modelos_individuales = historial.objects.get(id=pk)

        return render (request, 'modelos.html', {'modelo_individual':modelos_individuales})
    else:
        messages.error(request, 'Debes iniciar session.')
        return redirect ('inicio')

    - pasarlo al render 
    - y pasarlo a la plantilla 
```


12. Borrar Modelo ()
    - url int:pk
    - funcion - pk : (pass) 
    - no hace falta plantilla - indicar la platilla modelos cual borrar



13. Agregar Modelos ()
    - url (int:pk)
    - funcion (pass)
    - plantilla : agregar.html (basic)
    - formulario - Classe : ForAgregar
    - importalo a views
    - llamarlo en la funcion


14. Actualizar Modelos ()
    - urls (int-pk)
    - funcion (pass)
    - plantilla (basic)
    - funcion editar 
    - plantilla editar 
    - modelo.html poner el link para actualizar 



#### LOGIC SOFTWARE

15. Logica del software 
    - usamos el modelo.html no hace falta plantilla 
    - usamos url(modele) no hace falta url 
    - crear la funcion refactorizado 
    - Crear la funcion principal 
    - logica de sofware en la funcon principal 