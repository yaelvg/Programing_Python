import Examen1_2 as P
'''Funcionamiento de la clase Agenda

En resumen la clase Agenda contien un metodo "registro" el cual me ayuda a crear
instancias de la clase Contacto, esto me facilita poder agregarlas al atributo "listas"

'''

'''Se crea una instancia de tipo agenda que es la que contendra cada contacto'''
agenda_telefonica=P.Agenda()

'''Se manda a llamar el metodo de la clase Agenda y se inicializa con ciertos atributos'''
agenda_telefonica.registros('Alejandro', 5551533609)
agenda_telefonica.registros('Adis',5578980098)
agenda_telefonica.registros('Marco', 5567892178)

#Muestra los contactos en la la agenda
agenda_telefonica.contactos()
print('/////////////////')

#Elima los contactos de la agenda
agenda_telefonica.eliminar(2)
print('/////////////////')

#Se manda a llamar otra vez contactos para comprobar que se elimnino el contacto anterios
agenda_telefonica.contactos()
print('/////////////////')

#Busqued por nombre del contacto
agenda_telefonica.busqueda_nombre('x')
print('/////////////////')

#Busqued por nombre del contacto
agenda_telefonica.busqueda_numero(5551533609)
