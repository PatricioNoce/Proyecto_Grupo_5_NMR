# Generated by Django 4.1.2 on 2022-10-27 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nmr_food', '0006_alter_menu_precio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Informacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres_integrantes', models.CharField(max_length=100)),
            ],
        ),
    ]
