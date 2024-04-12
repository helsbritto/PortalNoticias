from django import forms
from base.models import Cadastro, Noticia

class CadastroForm(forms.ModelForm):
    class Meta:
        model = Cadastro
        fields = ['nome', 'email', 'senha']
        widgets = {'senha': forms.PasswordInput()}

class NoticiaForm(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = ['titulo', 'categoria', 'imagem', 'conteudo']