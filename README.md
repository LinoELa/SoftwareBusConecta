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




#### LOGIC

6. Primera Logica - (LogIn) Iniciar Session
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