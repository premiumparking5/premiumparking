# Generated by Django 5.2.3 on 2025-07-24 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mombre', models.TextField(verbose_name='nombre')),
                ('apellidos', models.TextField(verbose_name='apellidos')),
                ('rol_id', models.TextField(verbose_name='rol_id')),
            ],
        ),
    ]
