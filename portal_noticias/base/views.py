from django.shortcuts import render

# Create your views here.
def inicio(request):
    return HttpResponse('Ola Nicolas')

def listaNoticias(request):
    pass