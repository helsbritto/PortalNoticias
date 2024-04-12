from django.shortcuts import render
from django.http import HttpResponse 
from base.forms import CadastroForm
from base.models import Cadastro
from base.models import Noticia

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