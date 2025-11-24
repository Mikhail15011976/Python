import requests
import json
import time
from tqdm import tqdm
from pprint import pprint


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
        rez = req['response']['items']
        for i in tqdm(rez):
            time.sleep(1)
        return rez

    def sorted_photos(self):
        uploaded_photos = self.user_photos()
        photo_all_max = []
        for photo in uploaded_photos:

            photo_dict = {
                'file_name': f"{photo['likes']['count']}_{photo['date']}.jpg",
                'size': photo['sizes'][-1]['type'],
                'url': photo['sizes'][-1]['url']
            }
            photo_all_max.append(photo_dict)

        with open('data.json', 'w') as f:
            json.dump(photo_all_max, f, indent=4)

        return photo_all_max


class Yandex:
    base_host = 'https://cloud-api.yandex.net/'

    def __init__(self, token, folder):
        self.token = token
        self.folder = self.create_folder(folder)
        self.url = "https://cloud-api.yandex.net/v1/disk/resources/upload"

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def create_folder(self, folder):
        uri = 'v1/disk/resources'
        create_uri = self.base_host + uri
        params = {'path': folder}
        response = requests.put(create_uri, headers=self.get_headers(), params=params)
        if response.status_code == 201:
            print('Папка создана')
        else:
            print('Такая папка уже есть')
        return folder

    def upload_to_disk(self, t):
        for image in t:
            params = {
                'path': self.folder + '/' + image['file_name'],
                'url': image['url']
            }
            url = "https://cloud-api.yandex.net/v1/disk/resources/upload/"
            r = requests.post(url=url, params=params, headers=self.get_headers())
            for i in tqdm(r):
                time.sleep(1)
            res = r.json()
            print(json.dumps(res, sort_keys=True, indent=4, ensure_ascii=False))


if __name__ == '__main__':

    access_token = str(input("Введите токен VK \n -- "))
    TOKEN = str(input('Введите токен Яндекс диска \n -- '))
    user_id = str(input('Введите id пользователя VK \n -- '))

    vk = VK(access_token, user_id)
    uploading_photos = vk.sorted_photos()
    ya = Yandex(TOKEN, 'Фотографии с профилей VK')
    ya.upload_to_disk(uploading_photos)
    pprint(uploading_photos)
    print('Фотографии на яндекс диск загружены')

