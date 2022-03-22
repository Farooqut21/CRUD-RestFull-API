
import requests
data_id = input("Enter the product id you want to use \n")

try: 
    data_id = int(data_id)
except:
    data_id = None
    print(f'{data_id} not a valid ID')

if data_id:
    endpoint = f"http://localhost:8000/api/covid/{data_id}/delete"
    get_response = requests.delete(endpoint)
    print(get_response.status_code,get_response.status_code==204)
 