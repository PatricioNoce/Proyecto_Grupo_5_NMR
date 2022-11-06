# Generated by Django 4.1.2 on 2022-10-26 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nmr_food', '0002_configuracion_alter_cliente_direccion'),
    ]

    operations = [
        migrations.CreateModel(
            name='menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comida', models.CharField(choices=[('Tacos', 'tacos'), ('Hamburguesa', 'hamburguesa'), ('Pizza', 'pizza'), ('Empanadas', 'empanadas')], default='hamburguesa', max_length=20)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
    ]