from django.shortcuts import render

# Create your views here.
def Home(request):
    return render(request, 'home.html')  ##Renderiza nuestro archivo html

def Nosotros(request):
    return render(request, 'us.html')  ##Renderiza nuestro archivo html
