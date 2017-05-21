from roadwarrior.device.base import ServiceThread


class UltrasonicSensorService(ServiceThread):
    def __init__(self, flag, queue_out, sensors, freq=0.5):
        super(UltrasonicSensorService, self).__init__(flag, False, queue_out, freq)
        self.sensors = sensors

    def process(self):
        sensor_snapshot = []
        for sensor in self.sensors:
            sensor_snapshot.append((sensor.SENSOR_KEY, sensor.make_measurement()))

        self.queue_out.put(sensor_snapshot)


"""
class CameraService(ServiceThread):
    def __init__(self, flag, queue_out, sensors, freq):
        super(CameraService, self).__init__(flag, False, queue_out, freq)
        self.sensors = sensors

    def process(self):
        pass
"""
