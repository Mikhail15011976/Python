#Применить написанный логгер к приложению из любого предыдущего д/з.

import os
import types

def logger(old_function):
    def new_function(*args, **kwargs):

        import datetime
        with open('generator.log', 'w', encoding='utf-8') as f:
            result = old_function(*args, **kwargs)

            f.write(f'''
            Дата и время вызова функции {datetime.datetime.now()}\n,
            Имя функции "{old_function.__name__}"\n,
            Данные args {str(args)}\n,
            Данные kwargs {str(kwargs)}\n
            Возвращаемое значение функции {result}\n
            ''')

        return result

    return new_function

@logger
def Flat_generator(list_of_list):
    for i in list_of_list:
        for j in i:
            yield j

def test_2():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            Flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(Flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(Flat_generator(list_of_lists_1), types.GeneratorType)


if __name__ == '__main__':
    test_2()