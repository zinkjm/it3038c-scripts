import json
import requests

print('Please enter your zip code: ')
zip = input()

r = requests.get('http://api.openweathermap.org/data/2.5/weather?zip=%s,us&appid=827739d3585dfd85c361286f79ca5f8c' % zip)

data=r.json()
print(data['weather'][0]['description'])