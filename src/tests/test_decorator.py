import ddt

import unittest

from Homework6 import homework


@ddt.ddt
class DecoratorTest(unittest.TestCase):

    @ddt.data(
        (homework.func(2, 2), 4),
        (homework.func(2, 3), 5),
        (homework.func(3, 3), 6),
    )
    @ddt.unpack
    def test_sum(self, res, expected):
        """Assert that the homework.func correctly sums up 2 numbers"""
        self.assertEqual(res, expected)

    @ddt.data(
        ('a', 2),
        ([3, 5, 1], 2),
        ({2: 1, 3: 4}, 2),
    )
    @ddt.unpack
    def test_error(self, first_p, second_p):
        """Assert that TypeError is raised in case of wrong data type"""
        with self.assertRaises(TypeError):
            homework.func(first_p, second_p)

    def test_filecontent(self):
        """Assert results.txt has the correct data"""
        with open('results.txt', 'r') as f:
            for line in f:
                line_content = ' '.join(line.split()[1:3])
                self.assertEqual(line_content, 'is called')
