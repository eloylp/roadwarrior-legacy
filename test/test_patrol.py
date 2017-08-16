from unittest import TestCase

from ddt import ddt, file_data
from mock import Mock

from roadwarrior.device.sensor.service import UltrasonicSensorService
from roadwarrior.mediator.patrol import Patrol


@ddt
class TestPatrol(TestCase):
    @file_data('patrol.json')
    def test_run(self, sensors, expected_movements):
        mocked_sensors = []

        for sensor, measure in sensors.items():
            sensor_mock = Mock()
            sensor_mock.make_measurement.return_value = measure
            sensor_mock.SENSOR_KEY.return_value = sensor.upper()
            mocked_sensors.append(sensor_mock)

        sensor_service = UltrasonicSensorService(mocked_sensors)
        engine_mock = Mock()
        sut = Patrol(sensor_service, engine_mock)
        sut.make_step()

        for movement, args in expected_movements.items():
            engine_mock.process.assert_called_once_with(movement, args)
