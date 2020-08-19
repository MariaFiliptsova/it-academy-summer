import ddt
import unittest

from Homework6 import EilerProject


@ddt.ddt
class TestEiler(unittest.TestCase):

    @ddt.data(
        (EilerProject.f(342), 32),
        (EilerProject.f(15), 121),
        (EilerProject.f(121), 4),
    )
    @ddt.unpack
    def test_f(self, result, expected):
        '''Assert that the EilerProject.f works correctly'''
        self.assertEqual(result, expected)

    def test_error(self):
        '''Assert that ValueError is raised in case of wrong value passed'''
        with self.assertRaises(ValueError):
            EilerProject.f('slovo')

    @ddt.data(
        (EilerProject.sf(342), 5),
        (EilerProject.sf(15), 4),
        (EilerProject.sf(121), 4),
    )
    @ddt.unpack
    def test_sf(self, res, expect):
        '''Assert that the EilerProject.sf works correctly'''
        self.assertEqual(res, expect)

    def test_sf_value_error(self):
        '''Assert that ValueError is raised in case of wrong value passed'''
        with self.assertRaises(ValueError):
            EilerProject.sf('slovo')

    @ddt.data(
        (EilerProject.g(5), 25),
        (EilerProject.g(4), 15),
        (EilerProject.g(13), 144),
    )
    @ddt.unpack
    def test_g(self, res, expect):
        '''Assert that the EilerProject.g works correctly'''
        self.assertEqual(res, expect)

    @ddt.data(
        (EilerProject.sg(5), 7),
        (EilerProject.sg(4), 6),
        (EilerProject.sg(13), 9),
    )
    @ddt.unpack
    def test_sg(self, res, expect):
        '''Assert that the EilerProject.sg works correctly'''
        self.assertEqual(res, expect)

    @ddt.data(
        (EilerProject.solution(1, 21), 156),
        (EilerProject.solution(1, 15), 84),
        (EilerProject.solution(5, 30), 265),
    )
    @ddt.unpack
    def test_solution(self, res, expect):
        self.assertEqual(res, expect)
