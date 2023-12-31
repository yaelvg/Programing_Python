from pymongo import MongoClient
import gridfs
import cv2
import base64
import numpy as np

mongo_uri = 'mongodb://localhost'

cliente = MongoClient(mongo_uri)

db = cliente['Usuarios']
colecciones = db['Datos']
'''Si deseamos guardar datos lo hacemos en formato JSON en python es en forma de objeto'''


# * INSERTA DATOS A LA BASE DE DATOS UNO A UNO
#colecciones.insert_one({'_id': 2,'Correo': x})

img = cv2.imread("IPN.png")

 #Codificación de la imagen a base64
_, buffer = cv2.imencode('.png', img)
codificado = base64.b64encode(buffer)

# Almacenamiento en MongoDB usando GridFS
filename = 'img_user'
fs = gridfs.GridFS(db)
file_id = fs.put(codificado, filename=filename)
user_1={'username': 'Aleee', 'Correo': 'av@gmail.com','filename': filename, 'file_id': file_id}
user_2={'username': 'azulita', 'Correo': 'azul@gmail.com','filename': filename, 'file_id': file_id}

# Inserción de metadatos en la colección image

 # * INSERTA DATOS A LA BASE DE DATOS EN CONJUNTO
colecciones.insert_many([user_1, user_2])
db.image.insert_one({'filename': filename, 'file_id': file_id})


# * Busqueda de datos
#results = colecciones.find()

# * Busqueda especifica de datos
result = colecciones.find_one({'username': 'Aleee'})
print(result['username'])
print('\n\n')

# * Parte de la imagen

fs = gridfs.GridFS(db)

# Obtener el objeto GridOut correspondiente al archivo
file_obj = fs.find_one({'filename': filename})

# Obtener el contenido codificado en base64
codificado = file_obj.read()

# Decodificar el contenido base64
decoded = base64.b64decode(codificado)

# Convertir los datos decodificados a un array NumPy
buffer = np.frombuffer(decoded, dtype=np.uint8)

# Decodificar el array NumPy con OpenCV
imagen = cv2.imdecode(buffer, flags=cv2.IMREAD_UNCHANGED)

# Mostrar la imagen con OpenCV o con otras bibliotecas según sea necesario
cv2.imshow('Imagen Recuperada', imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()

# INSERTAR
#colecciones.insert_one({'username': 'adis', 'Correo': 'pelos@hotmail.com'})

#Actualizando
#colecciones.update_one({'username': 'Aleee'}, {'$set':{'username': 'Yaeeel', 'edad':20}})

#AGREGAGNDO CON NUMEROS
#colecciones.update_one({'username': 'adis'}, {'$inc': {'EDAD': 'Peliiis'}})
'''
X =colecciones.count_documents({})
print(X)
colecciones.delete_many({})
X =colecciones.count_documents({})
print(X)
'''