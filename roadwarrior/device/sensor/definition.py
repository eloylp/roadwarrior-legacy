# coding=utf-8

class Sensors(object):
    def __init__(self):
        pass

    FRONT_FRONT = "FRONT_FRONT"
    FRONT_LEFT = "FRONT_LEFT"
    FRONT_RIGHT = "FRONT_RIGHT"
    COMPASS = "COMPASS"
    INCLINOMETER = "INCLINOMETER"


class SensorSnapshot(object):
    def __init__(self):
        self.front_left = False
        self.front_front = False
        self.front_right = False
        self.compass = False
        self.inclinometer = False

    def add_measurement_from_sensor(self, sensor):
        sensor_key = sensor.sensor_key.lower()
        for position in self.__dict__:
            if position == sensor_key:
                setattr(self, position, sensor.make_measurement())
