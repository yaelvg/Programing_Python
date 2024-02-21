
#* Skills
#! Importe de los modulos, ya que pyyhon no puede generar ni correr json's
import json

skills = [
    "Atención al cliente",  # Interactuar efectivamente con los pasajeros, resolver dudas y problemas.
    "Manejo de equipaje",  # Cargar, descargar y manejar el equipaje con cuidado y eficiencia.
    "Operaciones de rampa",  # Incluye la gestión de la carga, la descarga y el abastecimiento de las aeronaves.
    "Conocimiento de seguridad y regulaciones",  # Entender y aplicar las normas de seguridad y regulaciones aeronáuticas.
    "Gestión de check-in y embarque",  # Manejar los procesos de facturación y embarque de pasajeros.
    "Habilidades de comunicación",  # Comunicarse claramente tanto con los pasajeros como con el equipo de vuelo y otros empleados.
    "Manejo de crisis y solución de problemas",  # Resolver problemas de manera efectiva bajo presión.
    "Conocimientos informáticos",  # Utilizar sistemas de reservas, check-in y gestión de equipajes.
    "Habilidad para trabajar en equipo",  # Colaborar eficazmente con otros miembros del personal para asegurar una operación fluida.
    "Flexibilidad y adaptabilidad",  # Adaptarse a diferentes situaciones, horarios cambiantes y necesidades operativas.
]

#Creacion del json, es un diccionario comparandolo en python
dic = {
    "Skilss": []
}
# * Ayade las skills 

for i in skills:
       dic['Skilss'].append({'Name': i})
       
print(dic)

archivo = 'skills.json'

with open(archivo, "w", encoding="utf-8") as archivo_json:
    json.dump(dic, archivo_json, ensure_ascii=False, indent=2)
    

