import json
import requests
from json import dumps


url = 'http://mark-cn-back01.msk.stage.mark.puls.local/api/warehouse/v1.0/order/a08b7805-b4a8-11ec-9d1e-f0597297ce4a/'

headers = {'Content-Type': 'application/json;charset',
           'X-BRANCH-ID': '00000000100852',
           'Authorization': 'token 74c089995c50ed0731e41530ca5d33b59050d51f'}


answer = requests.post(url, headers=headers)

print(answer)
response = answer.json()
print(response, sep='151515')
