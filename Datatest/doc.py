import json
from datetime import datetime, timedelta
import random as rand 

# * Documentos
documents = ['word', 'excel', 'json', 'pasport', ' license']
duration = [1,2,3,4,5]
staryears = [2019, 2020, 2022, 2023, 2024]

date = datetime(2024,2,21,0,0,0)
print('date:' + str(date))

nextdate = date + timedelta(days=1, hours= 1, seconds= 1)
print('nextdate:' + str(nextdate))

#creammos el formato

dic = {
 'documents':[]   
}

#LLenado


for document in documents:
    expedition = datetime(rand.choice(staryears),1,1,0,0,0)
    dic['document'].append({
        'Name': document,
        'Expedition': expedition.strftime('%Y-%n-%d')
    })