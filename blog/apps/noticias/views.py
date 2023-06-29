from django.shortcuts import render
from .models import Noticia
# Create your views here.
def ListarNoticas(request):
    contexto = {}

    n = Noticia.objects.all() ##~~ SELECT * FROM noticia_noticias
    contexto['noticias'] = n  ##Diccionario con todas las noticias

    return render (request, 'noticias/listar.html',contexto)

''' x = Noticia.objects.get(pk=1)  #WHERE 
    print(f'Mi primer noticia: {x}')'''

def NoticiaParticular(request,pk):
    contexto = {}

    n = Noticia.objects.get(pk=pk) #un solo objeto
    contexto['noticia'] = n  

    return render (request, 'noticias/detalle.html',contexto)