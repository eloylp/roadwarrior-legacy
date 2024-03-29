# coding=utf-8

from Adafruit_MotorHAT import Adafruit_MotorHAT

from roadwarrior.device.engine.definition import EngineLocation


class DCMotor(object):
    def __init__(self, motor_hat, motor_number):
        self.motor = motor_hat.getMotor(motor_number)

    def set_speed(self, speed):
        self.motor.setSpeed(speed)

    def advance_forward(self):
        self.motor.run(Adafruit_MotorHAT.FORWARD)

    def advance_backward(self):
        self.motor.run(Adafruit_MotorHAT.BACKWARD)

    def release(self):
        self.motor.run(Adafruit_MotorHAT.RELEASE)

    def brake(self):
        self.motor.run(Adafruit_MotorHAT.BRAKE)


class Engine(object):
    def __init__(self, engine_key, motor):
        """
        :type engine_key: str
        :type motor: DCMotor
        """
        self.engine_key = engine_key
        self.motor = motor


class EngineFactory(object):
    def __init__(self, hat_addr=0x60):
        self.motor_hat = Adafruit_MotorHAT(addr=hat_addr)

    def get_engines(self):
        return (
            Engine(EngineLocation.BACK_RIGHT, DCMotor(self.motor_hat, 1)),
            Engine(EngineLocation.FRONT_RIGHT, DCMotor(self.motor_hat, 2)),
            Engine(EngineLocation.FRONT_LEFT, DCMotor(self.motor_hat, 3)),
            Engine(EngineLocation.BACK_LEFT, DCMotor(self.motor_hat, 4))
        )
