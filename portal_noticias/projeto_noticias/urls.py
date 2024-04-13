# urls.py
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from base.views import inicio, cadastro, noticia, detalhes_noticia, noticias_politica, noticias_economia, noticias_esporte, noticias_entretenimento, adicionar_noticia

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio),
    path('cadastro/', cadastro),
    path('noticia/', noticia),
    path('noticia/<uuid:noticia_uuid>/', detalhes_noticia, name='detalhes_noticia'),  # Rota para detalhes de notícia com UUID
    path('politica/', noticias_politica),
    path('economia/', noticias_economia),
    path('esportes/', noticias_esporte),
    path('entretenimento/', noticias_entretenimento),
    path('adicionarnoticia/', adicionar_noticia),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
