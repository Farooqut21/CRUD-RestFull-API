import requests
headers = {'Authorization': 'Bearer b155ada97a63a981e108d1102858a55d029e26da'
}
endpoint = "http://localhost:8000/api/covid/1121212/"
get_response = requests.get(endpoint,headers=headers)
print(get_response.json())
#print(get_response.status_code)