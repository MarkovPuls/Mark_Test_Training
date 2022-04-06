import requests

url = 'https://swapi.dev/api/'

answer = requests.get(url)

print(answer)
response = answer.json()
print(response)
