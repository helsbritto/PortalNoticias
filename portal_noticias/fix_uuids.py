# fix_uuids.py

import os
import sys
import django

# Adicione o diretório base ao caminho do Python
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projeto_noticias.settings')
django.setup()

from base.models import Noticia
import uuid

def corrigir_uuids():
    noticias_com_problemas = Noticia.objects.filter(id__isnull=True)
    for noticia in noticias_com_problemas:
        try:
            noticia.id = uuid.uuid4()
            noticia.save()
        except ValueError as e:
            print(f"Aviso: Encontrado UUID inválido para notícia {noticia.id}: {e}")

if __name__ == '__main__':
    corrigir_uuids()
