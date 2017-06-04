from device.sensor.sensor import UltrasonicSensorSnapshot
from roadwarrior.device.base import ServiceThread


class UltrasonicSensorService(ServiceThread):
    def __init__(self, flag, queue_out, sensors):
        super(UltrasonicSensorService, self).__init__(flag, False, queue_out)
        self.sensors = sensors

    def process(self):
        sensor_snapshot = UltrasonicSensorSnapshot()
        for sensor in self.sensors:
            sensor_snapshot.add_Measurement_from_sensor(sensor)

        self.queue_out.put(sensor_snapshot)