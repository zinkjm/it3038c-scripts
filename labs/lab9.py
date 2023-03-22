import requests
import json

r = requests.get('http://localhost:3000/colors')

data = r.json()

for widget in data:
    name = widget['name']
    color = widget['color']
    print('%s is color %s \n' % (name, color))