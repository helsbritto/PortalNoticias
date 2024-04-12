from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from base.views import inicio, cadastro, noticia, noticias_politica, noticias_economia, noticias_esporte, noticias_entretenimento, adicionar_noticia

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio),
    path('cadastro/', cadastro),
    path('noticia/', noticia),
    path('politica/', noticias_politica),
    path('economia/', noticias_economia),
    path('esportes/', noticias_esporte),
    path('entretenimento/', noticias_entretenimento),
    path('adicionarnoticia/', adicionar_noticia),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
