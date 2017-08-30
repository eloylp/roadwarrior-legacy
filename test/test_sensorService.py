# coding=utf-8
from unittest import TestCase

import math

from mock import Mock

from roadwarrior.device.sensor.definition import Sensors
from roadwarrior.device.sensor.service import SensorService


class TestSensorService(TestCase):
    def setUp(self):

        self.sensors_to_mock = [
            Sensors.FRONT_RIGHT,
            Sensors.FRONT_FRONT,
            Sensors.FRONT_LEFT,
            Sensors.INCLINOMETER,
            Sensors.COMPASS
        ]
        sensors = []
        for sensor_key in self.sensors_to_mock:
            mock = Mock()
            mock.SENSOR_KEY = sensor_key
            mock.make_measurement = Mock(return_value=math.pi)
            sensors.append(mock)

        self.sensor_service = SensorService(sensors)

    def test_process(self):

        sensor_snapshot = self.sensor_service.process()
        for sensor in self.sensors_to_mock:
            self.assertEqual(math.pi, getattr(sensor_snapshot, sensor.lower()))

    def test_get_sensor_by_key(self):
        for key in self.sensors_to_mock:
            self.assertIsNotNone(self.sensor_service.get_sensor_by_key(key))

    def test_get_sensor_by_key_raise_on_not_found(self):
        self.assertRaises(KeyError, self.sensor_service.get_sensor_by_key, 'aaaa')
