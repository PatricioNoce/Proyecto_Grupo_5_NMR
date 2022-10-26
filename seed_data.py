from NMR_Food.models import menu

menu(Comida = 'taco', Precio = '$500') .save()
menu(Comida = 'hamburguesa', Precio = '$750') .save()
menu(Comida = 'pizza', Precio = '$600') .save()
menu(Comida = 'empanada', Precio = '$1200') .save()

print ("Estas son nuestras opciones")

