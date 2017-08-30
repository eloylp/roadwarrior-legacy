# coding=utf-8

import time


class AllStopMove(object):
    def __init__(self, engines):
        self.engines = engines

    def execute(self):
        for e in self.engines:
            e.motor.brake()
            e.motor.release()


class AllForwardMove(object):
    def __init__(self, engines):
        self.engines = engines

    def execute(self, speed):
        for e in self.engines:
            e.motor.set_speed(speed)
            e.motor.advance_forward()


class AllBackwardMove(object):
    def __init__(self, engines):
        self.engines = engines

    def execute(self, speed):
        for e in self.engines:
            e.motor.set_speed(speed)
            e.motor.advance_backward()


class TurnDegreesMove(object):
    def __init__(self, engines, heading_sensor):
        """
        :type sensor_service: roadwarrior.device.sensor.service.SensorService
        """
        self.engines = engines
        self.heading_sensor = heading_sensor

    # Todo, need to do calcs here. checking the motor by motor key not by modulus.
    def execute(self, speed, direction):

        # sensor_service.

        count = 1
        for e in self.engines:
            e.motor.brake()
            e.motor.release()
            e.motor.set_speed(speed)
            if count % 2 == 0:
                e.motor.advance_backward()
            else:
                e.motor.advance_forward()
            count += 1

        time.sleep(2)
        for e in self.engines:
            e.motor.brake()
            e.motor.release()
