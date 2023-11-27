from pymongo import MongoClient
import gridfs
import cv2
import base64
import numpy as np

mongo_uri = 'mongodb://localhost'

cliente = MongoClient(mongo_uri)
db = cliente.image

img = cv2.imread("IPN.png")

# Codificación de la imagen a base64
_, buffer = cv2.imencode('.png', img)
codificado = base64.b64encode(buffer)

# Almacenamiento en MongoDB usando GridFS
filename = 'test'
fs = gridfs.GridFS(db)
file_id = fs.put(codificado, filename=filename)

# Inserción de metadatos en la colección image
db.image.insert_one({'filename': filename, 'file_id': file_id})

#//////////////////////////////////////////////////////
# Nombre del archivo que deseas recuperar
filename = 'test'

# Acceso a GridFS
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