# Generated by Django 4.0.2 on 2022-06-23 00:35

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogos', '0005_disciplina_alter_livro_disciplina'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livro',
            name='imagem',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]