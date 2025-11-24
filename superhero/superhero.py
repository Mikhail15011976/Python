import requests

print('Задача №1')

url='https://akabab.github.io/superhero-api/api/all.json'

response = requests.get(url).json()
print(response)

superhero_list = ['Hulk', 'Captain America', 'Thanos']
super_hero = {}
for guys in superhero_list:
    for elements in response:
        if elements['name'] == guys:
            super_hero['guys'] = elements['name'], int(elements['powerstats']['intelligence'])
            print(super_hero)

max_intelligence_of_superhero = max(super_hero.values())
print('Герой с максимальным показателем интеллекта:  ', max_intelligence_of_superhero)

print('Задача №2')

from settings import TOKEN

class YaUploader:

    base_host = 'https://cloud-api.yandex.net/'

    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def upload(self, file_path: str):
        uri = 'v1/disk/resources/upload/'
        upload_url = self.base_host + uri
        params = {'path': 'file_list.txt', 'overwrite': True}
        resp = requests.get(upload_url, headers=self.get_headers(), params=params).json()
        upload_link = resp.get('href')
        response = requests.put(upload_link, data=open(path_to_file, 'rb'), headers=self.get_headers())
        print(response.status_code)
        if response.status_code == 201:
            print('Загрузка произведена успешно')

if __name__ == '__main__':

    path_to_file = 'C:/Users/Admin/Desktop/file_list.txt'
    token = TOKEN
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)


