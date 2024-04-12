# Generated by Django 4.2.11 on 2024-04-11 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('categoria', models.CharField(choices=[('PL', 'Política'), ('ECON', 'Economia'), ('ESP', 'Esportes'), ('ENTR', 'Entretenimento')], max_length=20)),
                ('imagem', models.ImageField(upload_to='imagens')),
                ('conteudo', models.TextField()),
            ],
        ),
        migrations.AlterModelOptions(
            name='cadastro',
            options={'ordering': ['-data'], 'verbose_name': 'Formulário de contato', 'verbose_name_plural': 'Formulários de contatos'},
        ),
    ]