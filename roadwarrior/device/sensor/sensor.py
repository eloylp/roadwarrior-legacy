import time
from RPi import GPIO

from device.sensor.definition import Sensors


class UltrasonicSensor:
    def __init__(self, sensor_key, pin_trigger, pin_echo):

        self.SENSOR_KEY = sensor_key
        self.PIN_TRIG = pin_trigger
        self.PIN_ECHO = pin_echo
        self.setup_sensor()

    def setup_sensor(self):

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.PIN_TRIG, GPIO.OUT)
        GPIO.setup(self.PIN_ECHO, GPIO.IN)
        GPIO.output(self.PIN_TRIG, False)

    def clean(self):

        GPIO.cleanup()

    def make_measurement(self):

        self.send_pulse()
        res = self.check_pulse_return_time()
        result_in_cm = self.do_math_cm(res[0], res[1])

        return result_in_cm

    def send_pulse(self):

        GPIO.output(self.PIN_TRIG, True)
        time.sleep(0.00001)
        GPIO.output(self.PIN_TRIG, False)

    def check_pulse_return_time(self):
        pulse_start = 0
        pulse_end = 0
        while GPIO.input(self.PIN_ECHO) == 0:
            pulse_start = time.time()
        while GPIO.input(self.PIN_ECHO) == 1:
            pulse_end = time.time()

        return pulse_start, pulse_end

    def do_math_cm(self, pstart, pend):

        duration = pend - pstart
        distance_meters = (duration * 343) / 2
        distance_cm = round((distance_meters * 100), 2)

        return distance_cm


class UltrasonicSensorBuilder:
    def get_ultrasonic_sensors(self):
        return (
            UltrasonicSensor(Sensors.DISTANCE_FRONT, 23, 24),
            UltrasonicSensor(Sensors.DISTANCE_BACK, 27, 22)
        )
