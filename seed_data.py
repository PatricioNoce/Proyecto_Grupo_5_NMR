from NMR_Food.models import Menu, Cliente

Menu(comida = 'taco', precio = "500").save()
Menu(comida = 'hamburguesa', precio = "750").save()
Menu(comida = 'pizza', precio = "600").save()
Menu(comida = 'empanadas', precio = "120").save()

print ("Estas son nuestras opciones")


Cliente(nombre = 'Juan', telefono = 47658798, mail = 'juan@gma.com', direccion = 'calle juan 2456').save()
Cliente(nombre = 'Marcelo', telefono = 47699798, mail = 'marcelo@gma.com', direccion = 'calle marcelo 2456').save()
Cliente(nombre = 'Hugo', telefono = 57658798, mail = 'hugo@gma.com', direccion = 'calle hugo 2456').save()
Cliente(nombre = 'Patricio', telefono = 63658298, mail = 'patricio@gma.com', direccion = 'calle patricio 2456').save()

print ("Clientes de prueba cargados correctamente")

