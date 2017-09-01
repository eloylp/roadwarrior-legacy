# coding=utf-8

from unittest import TestCase

from ddt import ddt, file_data, data, unpack
from mock import Mock, mock

from device.engine.engine import Engine
from device.engine.navigation import TargetHeadingCalculator, Direction
from roadwarrior.device.engine.definition import EngineLocation
from roadwarrior.device.engine.move import TurnDegreesMove


@ddt
class TestTurnDegreesMove(TestCase):
    def setUp(self):
        self.heading_sensor = Mock()

        self.positive_heading = None
        self.initial_heading = None
        self.actual_heading = None

        self.heading_sensor_make_measurement_calls = 0

        self.heading_sensor.make_measurement = self.make_measurement_incremental

        self.motor_front_left = Mock()
        self.motor_front_right = Mock()
        self.motor_back_left = Mock()
        self.motor_back_right = Mock()

        self.engines = [
            Engine(EngineLocation.FRONT_LEFT, self.motor_front_left),
            Engine(EngineLocation.FRONT_RIGHT, self.motor_front_right),
            Engine(EngineLocation.BACK_LEFT, self.motor_back_left),
            Engine(EngineLocation.BACK_RIGHT, self.motor_back_right)
        ]

        self.target_heading_calculator = TargetHeadingCalculator()

        self.sut = TurnDegreesMove(self.engines, self.heading_sensor, self.target_heading_calculator)

    def make_measurement_incremental(self):

        if self.heading_sensor_make_measurement_calls is 0:
            self.heading_sensor_make_measurement_calls += 1
            return self.actual_heading

        if self.positive_heading:
            self.actual_heading += 1
        else:
            self.actual_heading -= 1
        if self.actual_heading < 0:
            self.actual_heading += 360
        self.heading_sensor_make_measurement_calls += 1
        return self.actual_heading

    @file_data('turn_degrees_move_test_cases.yml')
    def test_execute(self, direction, desired_degrees, speed, start_heading_degrees, motor_calls_expectations):

        if direction == Direction.LEFT:
            self.positive_heading = False
        elif direction == Direction.RIGHT:
            self.positive_heading = True
        else:
            raise Exception('Invalid dataset, direction must be in Direction constant class')

        self.initial_heading = start_heading_degrees
        self.actual_heading = start_heading_degrees

        self.sut.execute(direction, desired_degrees, speed)

        target_heading = self.target_heading_calculator.calculate(self.initial_heading, desired_degrees, direction)
        self.assertTrue(self.sut.is_close_to(self.actual_heading, target_heading, self.sut.accuracy_degrees))

        for motor, call_data in motor_calls_expectations.items():
            calls = []
            for function_call_data in call_data:
                input_length = len(function_call_data)
                if input_length > 2:
                    pass
                function_call = getattr(mock.call, function_call_data[0])
                if input_length == 1:
                    call = function_call()
                elif input_length == 2:
                    call = function_call(*function_call_data[1])
                else:
                    raise Exception('Bad test case format.')
                calls.append(call)
            motor_mock = getattr(self, motor)
            motor_mock.assert_has_calls(calls, False)

    @data(
        (20, 21, 1, True),
        (19.99999, 21, 1, False),
        (20.99999, 21, 1, True),
    )
    @unpack
    def test_is_closed_to(self, value, target_value, delta, expected_result):
        result = self.sut.is_close_to(value, target_value, delta)
        if expected_result:
            self.assertTrue(result)
        else:
            self.assertFalse(result)
