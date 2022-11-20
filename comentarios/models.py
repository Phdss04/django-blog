from django.db import models
from posts.models import Post
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Comentario(models.Model):
    nome_comentario = models.CharField(max_length=100, verbose_name='Nome')
    email_comentario = models.EmailField(blank=False, verbose_name='Email')
    comentario = models.TextField(blank=False)
    post_comentario = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Post')
    usuario_comentario = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='Usuario')
    data = models.DateTimeField(default=timezone.now)
    publicado = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nome_comentario
    