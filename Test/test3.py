import unittest
import Functions
from Functions import people, shelf, list_doc, add_doc, move_doc_shelf, delete_doc


class Test_Functions(unittest.TestCase):

    def test_1people(self):
        self.assertEqual(people("10006"), 'Аристарх Павлов', 'Проверка работы функции')

    def test_2shelf(self):
        self.assertEqual(shelf('10006'), '2', 'Проверка работы функции')
        self.assertIs(shelf('10006'), '2', 'Проверка присутствия документа на определенной полке')

    def test_3list_doc(self):
        rez = list_doc()
        res_expected = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]
        self.assertEqual(rez, res_expected, 'Проверка работы функции')

    def test_4add_doc(self):
        add_doc('Multipass', '2921', 'Конон Варвар', '3')
        self.assertIn('2921', Functions.directories['3'], 'Проверка работы функции')
        self.assertIn('Конон Варвар', Functions.documents[3]['name'], 'Проверка работы функции')

    def test_delete_doc(self):
        delete_doc('2207 876234')
        self.assertNotIn('2207 876234', Functions.directories['1'], 'Проверка работы функции')


    def test_6move_doc_shelf(self):
        move_doc_shelf("11-2", "3")
        self.assertIn(Functions.documents[1]['number'], Functions.directories['3'], 'Проверка работы функции')
        self.assertNotEqual(Functions.directories, '4', 'Проверка работы функции, если нет целевой полки')
        self.assertNotEqual(Functions.documents, '111', 'Проверка работы функции, если перемещают несуществующий документ')



if __name__ == '__main__':
    unittest.main()


