import requests

url1 = 'http://api.weatherapi.com/v1/current.json?key=4cd5672383814ae0932211421231209&q=Wroclaw&aqi=no'

miasto = 'Berlin'

url2 = 'http://api.weatherapi.com/v1/current.json?key=4cd5672383814ae0932211421231209&q='+ miasto + '&aqi=no'
response_var1 = requests.get(url2)
json_var1 = response_var1.json()

# print(json_var1)

temp_c = json_var1.get('current').get('temp_c')
print(temp_c)

aura = json_var1.get('current').get('condition').get('text')
print(aura)

print('Aktualna pogoda w', miasto , 'to:',aura,". i mamy temperature", temp_c, 'stopni celcjusza')

#for ips in json_var1['current']:
#    print(f"aktualna temperatura wynosi: {ips['temp_c']}")
#    print(f"aktualna pogoda jest: , {ips['condition']}")