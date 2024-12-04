from django import forms
from .models import FileUpload

class FileUploadForm(forms.ModelForm):
    class Meta:
        model = FileUpload
        fields = ('file', )



class FileSelectionForm(forms.Form):
    file = forms.ModelChoiceField(
        queryset=FileUpload.objects.all(),
        empty_label="Selecione um arquivo",
        label="Arquivo Existente"
    )