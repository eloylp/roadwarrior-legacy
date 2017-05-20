import threading
from Queue import Queue

from device.base import ServiceThread
from device.sensor.definition import Sensors
from device.sensor.sensor import UltrasonicSensor


class UltrasonicSensorService(ServiceThread):
    def __init__(self, flag, queue_out, sensors, freq):
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

if __name__ == '__main__':

    p1 = UltrasonicSensor(Sensors.DISTANCE_FRONT, 23, 24)
    p2 = UltrasonicSensor(Sensors.DISTANCE_BACK, 27, 22)

    running_flag = threading.Event()
    running_flag.set()
    queue = Queue()

    sc = UltrasonicSensorService(running_flag, queue, [p1, p2], 0.001)
    sc.start()

    while running_flag.is_set():
        sensor_measure = queue.get(True)
        print(sensor_measure[0] + "-->" + str(sensor_measure[1]))
