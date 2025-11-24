list_of_lists_1 = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None]
]


class FlatIterator:
    def __init__(self, list_of_list):
        self._list_of_list = list_of_list
        self.i  = -1

    def __iter__(self):
        return self

    def __next__(self):
        all_list = sum(self._list_of_list, [])
        if len(all_list) -1 == self.i:
            raise StopIteration
        else:
            self.i += 1
            return all_list[self.i]

def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()

    for item in FlatIterator(list_of_lists_1):
        print(item)




