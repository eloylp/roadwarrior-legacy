# coding=utf-8

from roadwarrior.device.sensor.definition import SensorSnapshot


class SensorService(object):
    def __init__(self, sensors):
        self.sensors = sensors

    def process(self):
        sensor_snapshot = SensorSnapshot()
        for sensor in self.sensors:
            sensor_snapshot.add_measurement_from_sensor(sensor)
        return sensor_snapshot

    def get_sensor_by_key(self, sensor_key):

        for sensor in self.sensors:
            if sensor.SENSOR_KEY == sensor_key:
                return sensor
        raise KeyError

