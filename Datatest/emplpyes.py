import json

nombres_con_apellidos = [
    "Sofía Martínez",
    "Juan Pérez",
    "Miguel Ángel Rodríguez",
    "María García",
    "Lucía Hernández",
    "Antonio López",
    "Laura González",
    "Carlos Jiménez",
    "Alejandra Gómez",
    "Fernando Ruiz"
]

skills= []
with open('./skils.js', 'r', encoding='utf-8') as archivo_json:
    skills_json = json.load(archivo_json)
    
for skill in skills_json['Skills']:
    skills.append(skill['Name'])
    