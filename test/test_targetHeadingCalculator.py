# coding=utf-8

from unittest import TestCase
from ddt import ddt, data, unpack

from device.engine.navigation import TargetHeadingCalculator


@ddt
class TestTargetHeadingCalculator(TestCase):
    def setUp(self):
        self.sut = TargetHeadingCalculator()

    @data(
        (50, 20, 'AAAAAAA', KeyError),
        (50, 20, 'RIGHT', 70),
        (50, 150, 'RIGHT', 200),
        (50, 20, 'LEFT', 30),
        (50, 60, 'LEFT', 350),
        (350, 160, 'RIGHT', 150),
        (350, 150, 'LEFT', 200),
        (0, 1080, 'RIGHT', 0),
        (0, 1080, 'LEFT', 0),
        (0, 1090, 'LEFT', 350),
        (0, 1090, 'RIGHT', 10),
        (350, 1110.6, 'RIGHT', 20.6),
        (10, 1110.6, 'LEFT', 339.4),
    )
    @unpack
    def test_calculate(self, actual_heading_degrees, desired_heading_degrees, direction, expected_result):

        if type(expected_result) in [float, int]:
            result = self.sut.calculate(actual_heading_degrees, desired_heading_degrees, direction)
            self.assertEqual(expected_result, result)
        else:
            self.assertRaises(expected_result, self.sut.calculate, actual_heading_degrees, desired_heading_degrees, direction)
