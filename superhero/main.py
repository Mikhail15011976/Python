import requests
import time
from pprint import pprint

URL = 'https://api.vk.com/method/users.get'
params = {
    'user_ids': '1',
    'access_token': token, # токен и версия api являются обязательными параметрами во всех запросах к vk
    'v':'5.131'
}
res = requests.get(URL, params=params)
pprint(res.json())