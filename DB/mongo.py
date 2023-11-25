from pymongo import MongoClient

mongo_uri = 'mongodb://localhost'

cliente = MongoClient(mongo_uri)

db = cliente['Usuarios']
colecciones = db['Datos']
'''Si deseamos guardar datos lo hacemos en formato JSON en python es en forma de objeto'''
x='av192851@gmail.com'
'''
# * INSERTA DATOS A LA BASE DE DATOS UNO A UNO
#colecciones.insert_one({'_id': 2,'Correo': x})
user_1={'username': 'Aleee', 'Correo': 'av@gmail.com'}
user_2={'username': 'azulita', 'Correo': 'azul@gmail.com'}

 # * INSERTA DATOS A LA BASE DE DATOS EN CONJUNTO
colecciones.insert_many([user_1, user_2])
'''
# * Busqueda de datos
results = colecciones.find()

for r in results:
    print(r)

# * Busqueda especifica de datos
result = colecciones.find_one({'username': 'Aleee'})
print(result)

# INSERTAR
#colecciones.insert_one({'username': 'adis', 'Correo': 'pelos@hotmail.com'})

#Actualizando
#colecciones.update_one({'username': 'Aleee'}, {'$set':{'username': 'Yaeeel', 'edad':20}})

#AGREGAGNDO CON NUMEROS
#colecciones.update_one({'username': 'adis'}, {'$inc': {'EDAD': 'Peliiis'}})
X =colecciones.count_documents({})
print(X)
colecciones.delete_many({})
X =colecciones.count_documents({})
print(X)