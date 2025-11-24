import requests
import json
import time
from tqdm import tqdm
from pprint import pprint
access_token = ''
TOKEN = ''


class VK:
    base_host = 'https://api.vk.com/method/'

    def __init__(self, access_token, user_id, version='5.131'):
        self.token = access_token
        self.id = user_id
        self.version = version
        self.params = {'access_token': self.token, 'v': self.version}

    def user_photos(self):
        uri = 'photos.get'
        photos_url = self.base_host + uri
        params = {'owner_id': self.id, 'photo_sizes': 1, 'album_id': 'profile', 'extended': 1, 'count': 5}
        response = requests.get(photos_url, params={**self.params, **params})
        req = response.json()
        r = req['response']['items']
        for i in tqdm(r):
            time.sleep(1)
        return r

    def photo_all(self):
        r = self.user_photos()
        photo_all_max = []
        for value in r:

            photo_dict = {
                'file_name': f"{value['likes']['count']}_{value['date']}.jpg",
                'size': value['sizes'][-1]['type'],
                'url': value['sizes'][-1]['url']
            }
            photo_all_max.append(photo_dict)

        with open('data.json', 'w') as f:
            json.dump(photo_all_max, f, indent=4)

        return photo_all_max

user_id = ''


class Yandex:
    base_host = 'https://cloud-api.yandex.net/'

    def __init__(self, token, direct):
        self.token = token
        self.direct = self.create_direct(direct)
        self.url = "https://cloud-api.yandex.net/v1/disk/resources/upload"

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def create_direct(self, direct):
        uri = 'v1/disk/resources'
        create_uri = self.base_host + uri
        params = {'path': direct}
        response = requests.put(create_uri, headers=self.get_headers(), params=params)
        if response.status_code == 201:
            print('Папка создана')
        else:
            print('Такая папка уже есть')
        return direct

    def upload_to_disk(self, t):
        for image in t:
            params = {
                'path': self.direct + '/' + image['file_name'],
                'url': image['url']
            }
            url = "https://cloud-api.yandex.net/v1/disk/resources/upload/"
            r = requests.post(url=url, params=params, headers=self.get_headers())
            for i in tqdm(r):
                time.sleep(1)
            res = r.json()
            print(json.dumps(res, sort_keys=True, indent=4, ensure_ascii=False))


if __name__ == '__main__':
    vk = VK(access_token, user_id)
    t = vk.photo_all()
    ya = Yandex(TOKEN, 'Фотографии с профилей VK')
    ya.upload_to_disk(t)
    pprint(t)
    print('Фотографии на яндекс диск загружены')

