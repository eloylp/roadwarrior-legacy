from roadwarrior.device.sensor.sensor import UltrasonicSensorSnapshot


class UltrasonicSensorService(object):
    def __init__(self, sensors):
        self.sensors = sensors

    def process(self):
        sensor_snapshot = UltrasonicSensorSnapshot()
        for sensor in self.sensors:
            sensor_snapshot.add_measurement_from_sensor(sensor)
        return sensor_snapshot
