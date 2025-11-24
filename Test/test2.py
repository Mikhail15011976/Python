import requests
import json
import unittest
from ya_header import Yandex
TOKEN = ''

class Test_yandex_disk(unittest.TestCase):
    def test_create_direct(self):
        ya = Yandex(TOKEN)
        if ya.create_direct() == 409:
            self.assertEqual(ya.create_direct(), 409, 'Если папка уже создана')
        else:
            self.assertEqual(ya.create_direct(), 201, 'При условии создания новой папки')

if __name__ == '__main__':
    ya = Yandex(TOKEN)
    ya.create_direct()
    unittest.main()