from django.urls import path, include
from . import views

app_name = 'noticias'  ##Se crea el nombre de la app para que urls.py del proyecto lo pueda encontrar

urlpatterns = [
    ##URLS Aplicaciones
    path('', views.ListarNoticas, name='listar'),
]
