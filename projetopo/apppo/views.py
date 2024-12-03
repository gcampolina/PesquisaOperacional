from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def config(request):
    return render(request, 'config.html')

def resultados(request):
    return render(request, 'resultados.html')