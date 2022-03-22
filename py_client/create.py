import requests

headers = {'Authorization': 'Bearer b155ada97a63a981e108d1102858a55d029e26da'
}
endpoint = "http://localhost:8000/api/covid/"
data = {
    'iso_code':'PAK',
    'continent': 'Asia',
    'location': 'Pakistan',
    'tests_unit':'testperformed',
}

get_response = requests.post(endpoint,json=data,headers=headers)
print(get_response.json())
#print(get_response.status_code)