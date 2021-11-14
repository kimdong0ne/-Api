import requests
import json

url = 'http://apis.data.go.kr/6260000/BusanSoilCntmnInfoService/getSoilCntmnInfo'
key = 'Pt1QQm5SgIjjJO/OoLZwK+tROwnuPaDTP7tQ2H0kTgZLS57JsywrDeVvrxYt1VlA93UMKuQQQ2My0xILqClpQw=='
params ={'serviceKey' : key , 'pageNo' : '1', 'numOfRows' : '10', 'inspec_yy' : '2019', 'resultType' : 'json' }

response = requests.get(url, params=params)
data = json.read(response)
print(data)