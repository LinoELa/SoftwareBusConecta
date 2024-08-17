
# 3 B
from django.urls import path
# 3 B A 
from . import views


urlpatterns = [
    # 3 B B
    path('', views.home, name='home'),
    # 5 B - 10 para que cada uno solo vea su modelo 
    path('inicio', views.inicio, name='inicio'),
    # 6 A
    path('login', views.login_user, name='login'),
    # 7 A 
    path('logout/', views.logout_user, name='logout'),
    # 8 A
    path('register/', views.register_user, name='register'),
    # 11 A
    path('modelos/<int:pk>', views.modelos_user, name='modelos'),
    # 12 A
    path('borrar/<int:pk>', views.borrar_user, name='borrar'),
    # 13 A
    path('agregar', views.agregar_user, name='agregar'),
    # 14 A
    path('actualizar/<int:pk>', views.actualizar_user, name='actualizar'),





]
