import requests

import json


url = "https://petstore.swagger.io/v2"

params = {
    'status': 'available'
}
headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json'
}


"""Запрос Get"""
res = requests.get(f"{url}/pet/findByStatus?status={params.get('status')}", headers=headers)
if 'application/json' in res.headers['Content-Type']:
    print(res.json())
else:
    print(res.text)


"""Запрос Post создадим питомца"""
data = {
        "id": 0,
        "category": {
            "id": 0,
            "name": "cat"
        },
        "name": "doggie1234",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    }

res = requests.post(f"{url}/pet", headers=headers, data=json.dumps(data))
if 'application/json' in res.headers['Content-Type']:
    print(res.json())
else:
    print(res.text)

"""Запрос Put(исправим имя питомца)"""
data = {
        "id": res.json().get('id'),
        "category": {
            "id": 0,
            "name": "cat"
        },
        "name": "doggie",
        }

res = requests.put(f"{url}/pet", headers=headers, data=json.dumps(data))
if 'application/json' in res.headers['Content-Type']:
    print(res.json())
else:
    print(res.text)

"""Запрос Delete(удалим питомца)"""
pet_id = res.json().get('id')
res = requests.delete(f"{url}/pet/{pet_id}", headers=headers)
if 'application/json' in res.headers['Content-Type']:
    print(res.json())
else:
    print(res.text)
