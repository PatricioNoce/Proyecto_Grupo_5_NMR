# Generated by Django 4.1.2 on 2022-11-05 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nmr_food', '0014_menu_descripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='comida',
            field=models.CharField(max_length=20),
        ),
    ]
