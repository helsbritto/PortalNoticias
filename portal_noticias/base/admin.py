from django.contrib import admin
from base.models import Cadastro, Noticia
# Register your models here.

@admin.register(Cadastro)
class CadastroAdmin(admin.ModelAdmin):
    list_display = ['nome', 'email', 'data']
    search_fields = ['nome', 'email']
    list_filter = ['data']

@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'categoria']
    search_fields = ['titulo', 'categoria']

    