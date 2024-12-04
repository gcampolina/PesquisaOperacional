
from django.db import models
from django.core.exceptions import ValidationError

def validate_csv(file):
    if not file.name.endswith('.csv'):
        raise ValidationError('Somente arquivos CSV são permitidos.')
   
    
class FileUpload(models.Model):
    file = models.FileField(upload_to='uploads/',validators=[validate_csv])
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file.name
