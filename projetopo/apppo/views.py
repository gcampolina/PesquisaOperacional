from django.shortcuts import render

from projetopo.utils.solver_nutrientes import solver_nutrientes



# Create your views here.

def home(request):
    return render(request, 'home.html')

def config(request):
    return render(request, 'config.html')

def resultados(request):
    params = request.GET
    nutrientes = [
    ["Calorias", int(params.get("calorias")),-1],
    ["Proteínas",int(params.get("proteinas")),-1],
    ["Lipídios",int(params.get("lipidios_min")),int(params.get("lipidios_max"))],
    ["Carboidratos",int(params.get("carboidratos")),-1],
    ["Fibras",int(params.get("fibra")),-1],
    ["Calcio",int(params.get("calcio")),-1],
    ["Ferro",int(params.get("ferro")),-1],
    ["Sodio",int(params.get("sodio_min")),int(params.get("sodio_max"))],
    ["Vitamina C",int(params.get("vitamina-c")),-1]
    ]


    resultados = solver_nutrientes(nutrientes)

    return render(request, 'resultados.html', {"resultados":resultados})

