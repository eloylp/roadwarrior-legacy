class Sensors:
    def __init__(self):
        pass

    FRONT_FRONT = "FRONT_FRONT"
    FRONT_LEFT = "FRONT_LEFT"
    FRONT_RIGHT = "FRONT_RIGHT"
    RIGHT = "RIGHT"
    REAR_RIGHT = "REAR_RIGHT"
    REAR_REAR = "REAR_REAR"
    REAR_LEFT = "REAR_LEFT"
    LEFT = "LEFT"


class UltrasonicSensorSnapshot(object):
    def __init__(self):
        self.front_left = False
        self.front_front = False
        self.front_right = False
        self.right = False
        self.rear_right = False
        self.rear_rear = False
        self.rear_left = False
        self.left = False

    def add_measurement_from_sensor(self, sensor):

        for position in self.__dict__:
            sensor_key = sensor.SENSOR_KEY.lower()
            if position == sensor_key:
                setattr(self, position, sensor.make_measurement())
