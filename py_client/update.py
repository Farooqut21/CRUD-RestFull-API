import requests
endpoint = "http://localhost:8000/api/products/10/update"
data = {
    'title':"product updated v2 ",
    'price': 111,
}
get_response = requests.put(endpoint,json=data)
print(get_response.json())
#print(get_response.status_code)