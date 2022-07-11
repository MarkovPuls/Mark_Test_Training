import requests
import json


url = 'http://mark-cn-back01.msk.stage.mark.puls.local/api/warehouse/v1.0/data/store_sscc_extended/'

param = {
    'limit': '10'
}

headers_m = {
    'accept': 'application/json',
    'X-Branch-Id': '00000000100852',
    'X-Db-Path': 'Srvr=mow1srvvapp46;Ref=TEST_MSK;',
    'Content-Type': 'application/json',
    'Authorization': 'Token 74c089995c50ed0731e41530ca5d33b59050d51f'}

body_m = {
    "batch": "AVAST_502",
    "expiration_date": "2025-01-01",
    "gtin": "50754041389897"
}

auth = requests.post(url, headers=headers_m, json=body_m, params=param)
m = auth.status_code
r = auth.text
data = r.split('},"')
for temp in data:
    print(temp)
print(m)
# print(r)

