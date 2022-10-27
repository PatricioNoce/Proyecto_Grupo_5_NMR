from NMR_Food.models import menu

menu(comida = 'taco', precio = "$500").save()
menu(comida = 'hamburguesa', precio = "$750").save()
menu(comida = 'pizza', precio = "$600").save()
menu(comida = 'empanadas', precio = "$1200").save()

print ("Estas son nuestras opciones")

