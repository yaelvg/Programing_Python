import sqlite3

'''Creacion de la base de datos'''
conexion = sqlite3.connect("DB_1.db")

#! cursor
cursor = conexion.cursor()
'''Creacion de la table'''
# ? cursor.execute("CREATE TABLE usuarios (nombre VARCHAR(50), edad INTEGER, email VARCHAR(50))")



# ! Esta parte del codigo cuenta con un error, ya que cada que se ejeucta el script, vuelve a mandar
# ! los datos sin importar si hay repeticiones
#************************************************************************************************
'''Para poder agregar a la base de datos, datos necesitamos mandar los parametros y hacer un commit'''
#cursor.execute("INSERT INTO usuarios VALUES ('Alejandro', 20, 'yvaldezg@ipn.mx') ")
#* Siempre desde la conexion
#conexion.commit()
#************************************************************************************************


#************************************************************************************************
#Podemos mandar a llamar a los registros para poder tener accesso a la informacion en la DB
#cursor.execute("SELECT * FROM usuarios")
#usuarios = cursor.fetchall()
#print (usuarios) Devuelve una tupla
#************************************************************************************************

#* Agreagar de forma masiva cierto tipos de datos


#  Recordar guardar los cambios que se han realizados dede SQLite

usuario = [('Azul', 12, 'azuul@gmail.com'),('Ada', 18, 'adaval@gmail.com' )]
cursor.executemany("INSERT INTO usuarios VALUES (?,?,?)", usuario)

conexion.commit()

conexion.close()