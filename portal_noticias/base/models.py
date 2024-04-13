from django.db import models
import uuid

# Create your models here.
class Cadastro(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=75)
    senha = models.CharField(max_length=50)
    data = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.nome} [{self.email}]'
    class Meta:
        verbose_name = 'Formulário de contato'
        verbose_name_plural = 'Formulários de contatos'
        ordering = ['-data']
    
class Noticia(models.Model):
    CATEGORIA_NOTICIAS = (
        ('PL', 'Política'),
        ('ECON', 'Economia'),
        ('ESP', 'Esportes'),
        ('ENTR', 'Entretenimento'),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    titulo = models.CharField(max_length=255)
    categoria = models.CharField(max_length=20, choices=CATEGORIA_NOTICIAS)
    imagem = models.ImageField(upload_to='imagens')
    conteudo = models.TextField()

    def __str__(self):
        return self.titulo
    
    class Meta:
        verbose_name = 'Notícia'
        verbose_name_plural = 'Notícias'

