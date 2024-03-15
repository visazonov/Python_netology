# pip install pytest

from unittest import TestCase
import pytest
from decimal import Decimal

# from main import summarise
# from main import myltiply
# from main import get_dict

from tests.main_tests import summarise
from tests.main_tests import myltiply
from tests.main_tests import get_dict

# class TestSummarise(TestCase):
    # def test_with_positive_numbers(self):
    #     x, y = 10, 20
    #     res = summarise(x, y)
    #
    #     # assert res == 30
    #     self.assertEquals(res, 30)

    # def test_with_str_and_num(self):
    #     x, y = 20, '30'
    #     res = summarise(x, y)
    #     self.assertEquals(res, 50)

#     def test_with_negative_nums(self):
#         x, y = -10, -20
#         res = summarise(x, y)
#         self.assertEquals(res, -30)
# # >
#     def test_res_greater_than(self):
#         x, y = 10, 15
#         res = summarise(x, y)
#         self.assertGreater(res, 21)
#
# # <
#     def test_res_less_than(self):
#         x, y = 10, 15
#         res = summarise(x, y)
#         self.assertLess(res, 21)
#
# # >=
#     def test_res_greater_equal_than(self):
#         x, y = 10, 15
#         res = summarise(x, y)
#         self.assertGreaterEqual(res, 21)
#
# # <=
#     def test_res_less_equal_than(self):
#         x, y = 10, 15
#         res = summarise(x, y)
#         self.assertLessEqual(res, 21)
#
# # !=
#     def test_res_not_equal(self):
#         x, y = 10, 15
#         res = summarise(x, y)
#         self.assertNotEquals(res, 21)
#
# # is
#     def test_res_is(self):
#         x, y = 10, 15
#         res = summarise(x, y)
#         self.assertIs(res, 25)
#
# # not is
#     def test_res_not_is(self):
#         x, y = 10, 15
#         res = summarise(x, y)
#         self.assertIsNot(res, 35)
#
# # in
#     def test_res_in(self):
#         x, y = 10, 15
#         res = summarise(x, y)
#         self.assertIn(res, [24, 25, 26])
#
# # not in
#     def test_res_not_in(self):
#         x, y = 10, 15
#         res = summarise(x, y)
#         self.assertNotIn(res, [1, 2, 3])


# python -m unittest tests/test_funcs.py
# pytest tests\tests_funcs.py


# def test_myltiply_2_numbers():
#     x, y = 20, 10
#     expected_res = 200
#     res = myltiply(x,y)
#     assert res == expected_res
#
# def test_myltiply_num_list():
#     x, y = 29, [2]
#     expected_res = 58
#     res = myltiply(x,y)
#     # assert res != expected_res
#     # assert res is not expected_res
#     assert not isinstance(res, int)

@pytest.mark.parametrize('x, y, expected', [
    (10, 20, 200),
    (39, 2, 78),
    (-10, -20, 200),
    (29, Decimal('0.4'), Decimal('11.6')),
    (8, 3, 24)
])
def test_myltiply_with_nums(x, y, expected):
    res = myltiply(x, y)
    assert res == expected


def test_get_dict():
    res = get_dict()
    assert isinstance(res, dict)
    assert 'name' in res
    assert 'date' not in res
    assert ['name', 'age', 'city'] == list(res.keys())
    assert res['name'] == 'Ivan'


