import unittest
from task import task_1, task_2, task_3

class Test_task(unittest.TestCase):

    def test_task_1(self):
        rez = task_1()
        rez_expected = [
            {'visit1': ['Москва', 'Россия']}, {'visit3': ['Владимир', 'Россия']},
                        {'visit7': ['Тула', 'Россия']}, {'visit8': ['Тула', 'Россия']},
                        {'visit9': ['Курск', 'Россия']}, {'visit10': ['Архангельск', 'Россия']}
        ]
        self.assertEqual(rez, rez_expected, 'Проверка работы функции')
        self.assertIsInstance(rez, list, 'Результат функции должен быть list')

    def test_task_2(self):
        rez = task_2()
        rez_expected = [98, 35, 15, 213, 54, 119]
        self.assertEqual(rez, rez_expected, 'Проверка работы функции')
        self.assertIsInstance(rez, list, 'Результат функции должен быть list')

    def test_task_3(self):
        rez = task_3()
        rez_expected = 'yandex'
        self.assertEqual(rez, rez_expected, 'Проверка работы функции')
        self.assertIsInstance(rez, str, 'Результат функции должен быть str')

if __name__ == "__main__":
    unittest.main()