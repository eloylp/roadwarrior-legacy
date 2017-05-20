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


class EngineBuilder:
    def __init__(self, hat_addr=0x60):
        self.motor_hat = Adafruit_MotorHAT(addr=hat_addr)

    def get_engines(self):
        return (
            DCMotor(self.motor_hat, 1),
            DCMotor(self.motor_hat, 2),
            DCMotor(self.motor_hat, 3),
            DCMotor(self.motor_hat, 4)
        )
