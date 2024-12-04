from django.shortcuts import render, redirect, get_object_or_404
from .forms import FileSelectionForm, FileUploadForm
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .models import FileUpload
from projetopo.utils.solver_nutrientes import solver_nutrientes
from datetime import datetime
import pandas as pd
import os


# Create your views here.

def home(request):
    form = FileSelectionForm()
    return render(request, 'home.html',{'form': form})

def config(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = FileUploadForm()
    return render(request, 'config.html', {'form': form})
    

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
    file_id = params.get("file")
    file = get_object_or_404(FileUpload, id=file_id)
    base_name = file.file.name.split('/')[-1]

    try:
        resultados = solver_nutrientes(nutrientes,base_name)
    except:
        return render(request, 'erro.html')
    total = 0
    for resultado in resultados:
        total = total + resultado['price']
    total = round(total, 2)

    df = pd.DataFrame(resultados)

    # Salvar o DataFrame em um arquivo Excel
    filename =  datetime.today().strftime('%Y-%m-%d %H:%M:%S')+".xlsx"
    df.to_excel(os.path.join(settings.MEDIA_ROOT,filename), index=False)

    return render(request, 'resultados.html', {"resultados":resultados, "total":total,"filename":filename})
