import requests
from json import dumps

url = 'https://api.sb.mdlp.crpt.ru/api/v1/reestr/sscc/sscc_check'

headers = {'Content-Type': 'application/json;charset',
           'Host': 'api.sb.mdlp.crpt.ru',
           'Accept': 'application/json',
           'Authorization': 'token e4a47e7b-7845-4ac4-810d-0141f4772703'}


data = {'sscc': '141312311313113656'}

answer = requests.post(url, data=dumps(data), headers=headers, verify=False)

print(answer)
response = answer.json()
print(response)
