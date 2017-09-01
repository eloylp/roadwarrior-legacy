# coding=utf-8

from unittest import TestCase

from ddt import ddt, unpack, data

from device.sensor.sensor import InstrumentAdapterBase


@ddt
class TestInstrumentAdapterBase(TestCase):

    @data(
        (1.23, 1, 1.2),
        (-1.23, 1, -1.2),
        (-1, 1, -1),
        (-1, 1, -1),
        ((11.23, 12.36), 1, (11.2, 12.4)),
        ([11.23, 12.36], 1, (11.2, 12.4)),
        ('aaaa', 1, TypeError)
    )
    @unpack
    def test_adjust_precision(self, value, precision, expected_result):

        sut = InstrumentAdapterBase(precision=precision)
        if type(value) in [tuple, list, int, float]:
            result = sut.adjust_precision(value)
            self.assertEqual(expected_result, result)
        else:
            self.assertRaises(TypeError, sut.adjust_precision, value)
