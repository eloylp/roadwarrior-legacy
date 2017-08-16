from unittest import TestCase

from mock import MagicMock

from roadwarrior.device.sensor.definition import Sensors
from roadwarrior.device.sensor.sensor import UltrasonicSensorSnapshot


class TestUltrasonicSensorSnapshot(TestCase):
    @staticmethod
    def get_test_sensors():
        sensors = []
        for posible_sensor in Sensors.__dict__:
            if not posible_sensor.startswith('__'):
                sensor = MagicMock()
                sensor.make_measurement = MagicMock(return_value=100)
                sensor.SENSOR_KEY = posible_sensor
                sensors.append(sensor)

        return sensors

    def test_add_measurement_from_sensor(self):
        sensor_snapshot = UltrasonicSensorSnapshot()
        test_sensors = self.get_test_sensors()

        for sensor in test_sensors:
            sensor_snapshot.add_measurement_from_sensor(sensor)
        number_of_sensors = 0
        for sensor_name in sensor_snapshot.__dict__:
            if not sensor_name.startswith('__'):
                self.assertEquals(100, getattr(sensor_snapshot, sensor_name))
                number_of_sensors += 1
        self.assertEquals(len(test_sensors), number_of_sensors)
