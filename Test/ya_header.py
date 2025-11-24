import requests
import json
import unittest
TOKEN = ''

class Yandex:

    def __init__(self, token):
        self.token = token
        self.base_host = 'https://cloud-api.yandex.net/'

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def create_direct(self):
        uri = 'v1/disk/resources'
        create_uri = self.base_host + uri
        params = {'path': 'kuu661'}
        response = requests.put(create_uri, headers=self.get_headers(), params=params)
        return response.status_code

if __name__ == '__main__':
    ya = Yandex(TOKEN)
    print(ya.create_direct())