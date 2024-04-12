from django.shortcuts import render, redirect
from django.http import HttpResponse 
from base.forms import CadastroForm, NoticiaForm
from base.models import Cadastro, Noticia

# Create your views here.
def inicio(request):
    return render(request, 'inicio.html')

def cadastro(request):
    sucesso = False
    form = CadastroForm(request.POST or None)
    if form.is_valid():
        sucesso = True
        form.save()
    contexto = {
        'form': form,
        'sucesso': sucesso
    }
    return render(request, 'cadastro.html', contexto)

def listar_noticias_politica():
    noticias_politica = Noticia.objects.filter(categoria='PL')
    return noticias_politica

def noticias_politica(request):
    # Lista de notícias de política
    noticias_politica = listar_noticias_politica()
    return render(request, 'noticiaPolitica.html', {'noticias': noticias_politica})

def adicionar_noticia(request):
    if request.method == 'POST':
        form = NoticiaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('SUCESSO') #redirect('pagina_sucesso')  
        # Redirecionar para uma página de sucesso após adicionar a notícia
    else:
        form = NoticiaForm()
    
    return render(request, 'adicionar_noticia.html', {'form': form})