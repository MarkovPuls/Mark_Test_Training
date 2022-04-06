import requests
import json

url = 'https://api.sb.mdlp.crpt.ru/api/v1/auth/'
headers = {'Content-Type': 'application/json;charset'}
data = {'client_id': '2cabd9b7-6042-40d8-97c2-8627f5704aa1', 'client_secret': '1713da9a-2042-465c-80ba-4da4dca3323d',
        'user_id': 'b73abaa26e48bac2af6e0528178ba8f25edea048', 'auth_type': 'SIGNED_CODE'}

answer = requests.post(url, data=json.dumps(data), headers=headers)

print(answer)
response = answer.json()
print(response)