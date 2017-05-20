from Adafruit_MotorHAT import Adafruit_MotorHAT


class DCMotor:
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
