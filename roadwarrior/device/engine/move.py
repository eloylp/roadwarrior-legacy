# coding=utf-8

import time


class AllStopMove(object):
    def __init__(self, motors):
        self.motors = motors

    def execute(self):
        for m in self.motors:
            m.brake()
            m.release()


class AllForwardMove(object):
    def __init__(self, motors):
        self.motors = motors

    def execute(self, speed):
        for m in self.motors:
            m.set_speed(speed)
            m.advance_forward()


class AllBackwardMove(object):
    def __init__(self, motors):
        self.motors = motors

    def execute(self, speed):
        for m in self.motors:
            m.set_speed(speed)
            m.advance_backward()


class TurnDegreesMove(object):
    def __init__(self, motors):
        self.motors = motors

    # Todo, need to do calcs here. checking the motor by motor key not by modulus.
    def execute(self, speed):
        count = 1
        for m in self.motors:
            m.brake()
            m.release()
            m.set_speed(speed)
            if count % 2 == 0:
                m.advance_backward()
            else:
                m.advance_forward()
            count += 1

        time.sleep(1)
        for m in self.motors:
            m.brake()
            m.release()
