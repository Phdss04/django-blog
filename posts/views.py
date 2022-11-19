from django.shortcuts import redirect, render
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView

from categorias.models import Categoria
from comentarios.models import Comentario
from .models import Post
from django.db.models import Q, Case, When, Count
from comentarios.forms import FormComentario
from django.contrib import messages

# Create your views here.
class PostIndex(ListView):
    model = Post #model utilizado
    template_name = 'posts/index.html' #caminho do template que será utilizado
    paginate_by = 4 #númer  o de posts por página
    context_object_name = 'posts' #nome do objeto dentro do template
    def get_queryset(self):
        queryset = super().get_queryset().filter(publicado = True).order_by('-id')
        queryset = queryset.annotate(
            num_comentarios = Count(
                Case(
                    When(comentario__publicado = True, then=1)
                )
            )
        )
        return queryset

class PostBusca(PostIndex):
    template_name = 'posts/post_busca.html'
    def get_queryset(self):
        queryset = super().get_queryset()
        termo = self.request.GET.get('termo')
        
        if not termo:
            return queryset
        
        queryset = queryset.filter(
            Q(titulo__icontains = termo) | 
            Q(autor__first_name__iexact = termo) | 
            Q(conteudo__icontains = termo) | 
            Q(excerto__icontains = termo) | 
            Q(categoria__nome__iexact = termo)
        )
        return queryset
            
class PostCategoria(PostIndex):
    template_name = 'posts/post_categoria.html'
    def get_queryset(self):
        queryset = super().get_queryset()
        categoria = self.kwargs.get('categoria', None)
        queryset = queryset.filter(categoria__nome= categoria)
        return queryset  

class PostDetalhes(UpdateView):
    template_name = 'posts/post_detalhes.html'
    model = Post
    form_class = FormComentario
    context_object_name = 'post'
    
    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        post = self.get_object()
        comentarios = Comentario.objects.filter(publicado = True, post_comentario = post.id)
        contexto['comentarios'] = comentarios
        return contexto
    
    def form_valid(self, form):
        post = self.get_object()
        comentario = Comentario(**form.cleaned_data)
        comentario.post_comentario = post
        if self.request.user.is_authenticated:
            comentario.usuario_comentario = self.request.user
        comentario.save()
        messages.success(self.request, "Comentario enviado com sucesso!")
        return redirect('post_detalhes', pk=post.id)