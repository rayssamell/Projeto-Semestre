# Generated by Django 4.0.2 on 2022-06-22 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogos', '0002_remove_disciplina_descricao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disciplina',
            name='nome',
            field=models.CharField(max_length=100),
        ),
    ]
