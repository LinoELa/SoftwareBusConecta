
# 3 B
from django.urls import path
#  3 B A 
from . import views


urlpatterns = [
    #  3 B B
    path('', views.home, name='home')
]
