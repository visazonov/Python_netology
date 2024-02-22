import types
from itertools import chain

# Задание 1
# class FlatIteratorV1:

# def __init__(self, list_of_list):
#     self.list_of_list = list_of_list
#
# def __iter__(self):
#     self.count = -1
#     self.cursor = 0
#     return self
#
# def __next__(self):
#     self.count += 1
#     if len(self.list_of_list[self.cursor]) <= self.count:
#         self.count = 0
#         self.cursor += 1
#
#     if self.cursor >= len(self.list_of_list):
#         print('ууу')
#         raise StopIteration
#
#     return self.list_of_list[self.cursor][self.count]

# Задание 1
# class FlatIteratorV1:
#
#     def __init__(self, list_of_list):
#         self.list_of_list = list_of_list
#
#     def __iter__(self):
#         self.iterators = iter(iter(l) for l in self.list_of_list)  #3 списка
#         self.current_iter = next(self.iterators)                   #1-й итератор (список)
#         return self
#
#     def __next__(self):
#         try:
#             next_item = next(self.current_iter)      # проходим по 1 списку
#         except StopIteration:
#             self.current_iter = next(self.iterators)   # 2-й список, пото 3 список
#             next_item = next(self.current_iter)        # 1-й эл 2-й список итд
#         return next_item

# Задание 1
# class FlatIteratorV1:
#
#     def __init__(self, list_of_list):
#         self.list_of_list = list_of_list
#
#     def __iter__(self):
#         self.flat_iter = chain.from_iterable(self.list_of_list)
#         return self
#
#     def __next__(self):
#         return next(self.flat_iter)


# Задание 1
class FlatIteratorV1:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        return chain.from_iterable(self.list_of_list)


def test_1():

    list_of_lists_1 = [["a", "b", "c"], ["d", "e", "f", "h", False], [1, 2, None]]

    for flat_iterator_item, check_item in zip(
        FlatIteratorV1(list_of_lists_1),
        ["a", "b", "c", "d", "e", "f", "h", False, 1, 2, None],
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIteratorV1(list_of_lists_1)) == ["a", "b", "c", "d", "e", "f", "h", False, 1, 2, None]


###########################
# Задание 2
def flat_generator(list_of_lists):
    for i in list_of_lists:
        for item in i:
            yield item


# Задание 2
# def flat_generator(list_of_lists):
#     for i in list_of_lists:
#         yield from i

# Задание 2
# def flat_generator(list_of_lists):
#     for item in chain.from_iterable(list_of_lists):
#         yield item

# Задание 2
# def flat_generator(list_of_lists):
#     return (item for item in chain.from_iterable(list_of_lists))


def test_2():

    list_of_lists_1 = [["a", "b", "c"], ["d", "e", "f", "h", False], [1, 2, None]]

    for flat_iterator_item, check_item in zip(
        flat_generator(list_of_lists_1),
        ["a", "b", "c", "d", "e", "f", "h", False, 1, 2, None],
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ["a", "b", "c", "d", "e", "f", "h", False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)


# Задание 3
class FlatIteratorHard:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.iters_stack = [iter(self.list_of_list)]
        return self

    def __next__(self):
        while self.iters_stack:
            try:
                next_item = next(self.iters_stack[-1])
                #  пытаемся получить следующий элемент
            except StopIteration:
                self.iters_stack.pop()
                #  если не получилось, значит итератор пустой
                continue

            if isinstance(next_item, list):
                # если следующий элемент оказался списком, то
                # добавляем его итератор в стек
                self.iters_stack.append(iter(next_item))

            else:
                return next_item
        raise StopIteration


def test_3():

    list_of_lists_2 = [
        [["a"], ["b", "c"]],
        ["d", "e", [["f"], "h"], False],
        [1, 2, None, [[[[["!"]]]]], []],
    ]

    for flat_iterator_item, check_item in zip(
        FlatIteratorHard(list_of_lists_2),
        ["a", "b", "c", "d", "e", "f", "h", False, 1, 2, None, "!"],
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIteratorHard(list_of_lists_2)) == ["a", "b", "c", "d", "e", "f", "h", False, 1, 2, None, "!"]


# Задание 4


def flat_generator_v5(list_of_list):
    for i in list_of_list:
        if isinstance(i, list):
            for j in flat_generator_v5(i):
                yield j
        else:
            yield i


def test_4():
    list_of_lists_2 = [
        [["a"], ["b", "c"]],
        ["d", "e", [["f"], "h"], False],
        [1, 2, None, [[[[["!"]]]]], []],
    ]

    for flat_iterator_item, check_item in zip(
        flat_generator_v5(list_of_lists_2),
        ["a", "b", "c", "d", "e", "f", "h", False, 1, 2, None, "!"],
    ):
        assert flat_iterator_item == check_item

    assert list(flat_generator_v5(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']

    assert isinstance(flat_generator_v5(list_of_lists_2), types.GeneratorType)


if __name__ == "__main__":
    test_1()
    # test_2()
    # test_3()
    # test_4()
