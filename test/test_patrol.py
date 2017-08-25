# coding=utf-8

from unittest import TestCase

from ddt import ddt, file_data
from mock import Mock, mock

from roadwarrior.device.sensor.service import SensorService
from roadwarrior.mediator.patrol import Patrol


@ddt
class TestPatrol(TestCase):
    @file_data('patrol_test_cases.json')
    def test_run(self, sensors, expected_movements):
        mocked_sensors = []

        for sensor, measure in sensors.items():
            sensor_mock = Mock()
            sensor_mock.make_measurement.return_value = measure
            sensor_mock.SENSOR_KEY = sensor.upper()
            mocked_sensors.append(sensor_mock)

        sensor_service = SensorService(mocked_sensors)
        engine_service_mock = Mock()
        sut = Patrol(sensor_service, engine_service_mock)
        sut.make_step()

        self.assertEqual(len(expected_movements), len(engine_service_mock.method_calls),
                         "Different call count expected.")

        calls = []
        for movement in expected_movements:
            function = getattr(mock.call, 'process')
            input_length = len(movement)
            if input_length is 1:
                call = function(tuple(movement))
            elif input_length is 2:
                composition = (movement[0], tuple(movement[1]))
                call = function(composition)
            else:
                raise Exception('Bad test case format.')
            calls.append(call)

        engine_service_mock.assert_has_calls(calls, False)
