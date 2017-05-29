import requests


input_method = 'add'

payload = { 'method': input_method, 'upc':  '058807422839' }

r = requests.post('http://localhost:3000/api', data=payload)

print payload
print r.status_code
