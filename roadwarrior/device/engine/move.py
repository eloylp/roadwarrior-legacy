import time


class Descriptor:
    STOP = "STOP"
    FORWARD = "FORWARD"
    BACKWARD = "BACKWARD"
    TURN = "TURN"


class AllStop:
    def __init__(self, motors):
        self.motors = motors

    def execute(self):
        for m in self.motors:
            m.brake()
            m.release()


class AllForwardMove:
    def __init__(self, motors):
        self.motors = motors

    def execute(self, speed):
        for m in self.motors:
            m.set_speed(speed)
            m.advance_forward()


class AllBackwardMove:
    def __init__(self, motors):
        self.motors = motors

    def execute(self, speed):
        for m in self.motors:
            m.set_speed(speed)
            m.advance_backward()


class TurnDegreeesMove:
    def __init__(self, motors):
        self.motors = motors

    def execute(self, speed, degrees):
        for m in self.motors:
            m.brake()
            m.release()
            m.set_speed(speed)
        time.sleep(0.3 * degrees)
        for m in self.motors:
            m.brake()
            m.release()
