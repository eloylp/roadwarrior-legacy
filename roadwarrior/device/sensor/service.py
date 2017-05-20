from roadwarrior.device.base import ServiceThread


class UltrasonicSensorService(ServiceThread):
    def __init__(self, flag, queue_out, sensors, freq=0.5):
        super(UltrasonicSensorService, self).__init__(flag, False, queue_out, freq)
        self.sensors = sensors

    def process(self):
        for sensor in self.sensors:
            self.queue_out.put((sensor.SENSOR_KEY, sensor.make_measurement()))


"""
class CameraService(ServiceThread):
    def __init__(self, flag, queue_out, sensors, freq):
        super(CameraService, self).__init__(flag, False, queue_out, freq)
        self.sensors = sensors

    def process(self):
        pass
"""