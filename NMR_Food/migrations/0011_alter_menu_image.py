# Generated by Django 4.1.2 on 2022-11-02 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nmr_food', '0010_alter_menu_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
    ]
