# Generated by Django 2.1.3 on 2018-11-19 12:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('milonga', '0002_add_hora_inicio_hora_fim_milonga'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Tanda',
            new_name='Danca',
        ),
        migrations.RenameField(
            model_name='pardanca',
            old_name='tanda',
            new_name='danca',
        ),
    ]
