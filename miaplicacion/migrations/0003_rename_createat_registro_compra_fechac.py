# Generated by Django 5.0.6 on 2024-10-26 16:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('miaplicacion', '0002_deportivo_imagen'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registro_compra',
            old_name='createAt',
            new_name='fechaC',
        ),
    ]
