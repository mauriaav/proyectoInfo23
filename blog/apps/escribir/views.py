from django.shortcuts import render

# Create your views here.
def Escribir(request):
    nombres = ['Juan', 'Pedro', 'Lucas']
    return render (request, 'escribir/escribir.html',{'nombres': nombres})