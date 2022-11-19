from django.contrib import admin
from .models import Comentario

# Register your models here.
class ComentarioAdmin(admin.ModelAdmin):
    list_display= ['id', 'nome_comentario', 'email_comentario', 'post_comentario', 'data', 'publicado']
    list_editable = ['publicado']
    list_display_links= ['id', 'nome_comentario', 'email_comentario']

admin.site.register(Comentario, ComentarioAdmin)