from django.db import models

# Create your models here.
class Categoria(models.Model):
    nome = models.CharField(max_length=70, blank=False, default=None)
    
    def __str__(self):
        return self.nome
    