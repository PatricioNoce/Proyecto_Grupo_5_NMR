# Generated by Django 4.1.2 on 2022-11-02 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nmr_food', '0008_alter_menu_comida'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='posts'),
        ),
    ]