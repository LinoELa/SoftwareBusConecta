
# 3 B
from django.urls import path
# 3 B A 
from . import views


urlpatterns = [
    # 3 B B
    path('', views.home, name='home'),
    # 5 B 
    path('inicio/', views.inicio, name='inicio'),
    # 6 A
    path('login/', views.login_user, name='login'),


]
