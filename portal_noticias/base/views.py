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

def noticia(request):
    return render(request, 'noticia.html')

def listar_noticias_politica():
    noticias_politica = Noticia.objects.filter(categoria='PL')
    return noticias_politica

def noticias_politica(request):
    # Lista de notícias de política
    noticias_politica = listar_noticias_politica()
    return render(request, 'noticiaPolitica.html', {'noticiaspolitica': noticias_politica})

def listar_noticias_economia():
    noticias_economia = Noticia.objects.filter(categoria='ECON')
    return noticias_economia

def noticias_economia(request):
    # Lista de notícias de economia
    noticias_economia = listar_noticias_economia()
    return render(request, 'noticiaEconomia.html', {'noticiaseconomia': noticias_economia})

def listar_noticias_entretenimento():
    noticias_entretenimento = Noticia.objects.filter(categoria='ENTR')
    return noticias_entretenimento

def noticias_entretenimento(request):
    # Lista de notícias de entretenimento
    noticias_entretenimento = listar_noticias_entretenimento()
    return render(request, 'noticiaEntretenimento.html', {'noticiasentretenimento': noticias_entretenimento})

def listar_noticias_esporte():
    noticias_esporte = Noticia.objects.filter(categoria='ESP')
    return noticias_esporte

def noticias_esporte(request):
    # Lista de notícias de esporte
    noticias_esporte = listar_noticias_esporte()
    return render(request, 'noticiaEsporte.html', {'noticiasesporte': noticias_esporte})

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