from django.shortcuts import render

# Create your views here.
def ListarNoticas(request):
    return render (request, 'noticias/listar.html')