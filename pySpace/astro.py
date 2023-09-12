import requests

response_var = requests.get('http://api.open-notify.org/astros.json')
json_var = response_var.json()

print(json_var)

for ipeople in json_var['people']:
    print(ipeople['name'])