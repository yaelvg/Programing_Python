import json
# *Necesito los skills

ruta= './skills.json'

with open(ruta, "r", encoding='utf-8') as archivo_json:
    skills=json.load(archivo_json)
print(skills)


# * Hacemos la lista de los spots

spots = list()

for skill in skills['Skilss']:
    spots.append(skill['Name']+ '_spot')
print(spots)

dic= {
    'Spots': [
        
    ]
}

for index, spot in enumerate(spots):
    dic['Spots'].append({
        'Name': spot,
        'Skills':[skills['Skilss'][index]['Name']]
    })
    
#*Guardamos el json

nombredelarchivo= 'spot_json'
with open(nombredelarchivo, 'w', enconding = 'utf-8') as archivo_json:
    skills=json.load(archivo_json)