from pymongo import MongoClient
import gridfs
import cv2
import base64
import numpy as np

mongo_uri = 'mongodb://localhost'

cliente = MongoClient(mongo_uri)

db = cliente['Usuarios']
colecciones = db['Datos']

img1 = cv2.imread("IPN.png")
img2 = cv2.imread("lenna.ppm")

#Codificación de la imagen a base64
_, buffer1 = cv2.imencode('.png', img1)
_, buffer2 = cv2.imencode('.ppm', img2)

codificado1 = base64.b64encode(buffer1)
codificado2 = base64.b64encode(buffer2)

# Almacenamiento en MongoDB usando GridFS
filename1 = 'img_user1'
filename2 = 'img_user2'

fs = gridfs.GridFS(db)

file_id1 = fs.put(codificado1, filename=filename1)
file_id2 = fs.put(codificado2, filename=filename2)

user_1={'username': 'Aleee', 'Correo': 'av@gmail.com','filename': filename1, 'file_id': file_id1}
user_2={'username': 'azulita', 'Correo': 'azul@gmail.com','filename': filename2, 'file_id': file_id2}

# Inserción de metadatos en la colección image

 # * INSERTA DATOS A LA BASE DE DATOS EN CONJUNTO
colecciones.insert_many([user_1, user_2])
db.Datos.insert_one({'filename': filename1, 'file_id': file_id1})
db.Datos.insert_one({'filename': filename2, 'file_id': file_id2})


# * Busqueda de datos
#results = colecciones.find()

# * Busqueda especifica de datos
result = colecciones.find_one({'username': 'Aleee'})
print(result['username'])
print('\n\n')

# * Parte de la imagen

fs = gridfs.GridFS(db)

# Obtener el objeto GridOut correspondiente al archivo
file_obj1 = fs.find_one({'filename': filename1})
file_obj2 = fs.find_one({'filename': filename2})

# Obtener el contenido codificado en base64
codificado1 = file_obj1.read()
codificado2 = file_obj2.read()

# Decodificar el contenido base64
decoded1 = base64.b64decode(codificado1)
decoded2 = base64.b64decode(codificado2)

# Convertir los datos decodificados a un array NumPy
buffer1 = np.frombuffer(decoded1, dtype=np.uint8)
buffer2 = np.frombuffer(decoded2, dtype=np.uint8)

# Decodificar el array NumPy con OpenCV
imagen1= cv2.imdecode(buffer1, flags=cv2.IMREAD_UNCHANGED)
imagen2 = cv2.imdecode(buffer2, flags=cv2.IMREAD_UNCHANGED)

# Mostrar la imagen con OpenCV o con otras bibliotecas según sea necesario
cv2.imshow('Imagen Recuperada', imagen1)
#cv2.imshow('Imagen Recuperada', imagen2)
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