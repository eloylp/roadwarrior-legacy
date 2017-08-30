# coding=utf-8

from unittest import TestCase

from mock import Mock

from device.engine.definition import Direction
from device.engine.move import TurnDegreesMove


class TestTurnDegreesMove(TestCase):
    def setUp(self):

        self.heading_sensor = Mock()
        self.heading_sensor.make_measurement = Mock(return_value=60.34)

        self.motor_1 = Mock()
        self.motor_2 = Mock()
        self.motor_3 = Mock()
        self.motor_4 = Mock()

        self.motors = [self.motor_1, self.motor_2, self.motor_3, self.motor_4]

        self.movement = TurnDegreesMove(self.motors, self.heading_sensor)

    def test_execute_right(self):

        self.movement.execute(20, Direction.RIGHT)

        self.motor_1


