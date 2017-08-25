# coding=utf-8

import time

import Adafruit_LSM303
from Adafruit_LSM303 import LSM303
from Adafruit_LSM303.instruments import Compass, Inclinometer
from RPi import GPIO

from roadwarrior.device.sensor.definition import Sensors


class UltrasonicSensor(object):
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


class SensorFactory(object):
    @staticmethod
    def get_sensors():

        instrument_factory = InstrumentsFactory()
        return (
            UltrasonicSensor(Sensors.FRONT_LEFT, 27, 22),
            UltrasonicSensor(Sensors.FRONT_FRONT, 23, 24),
            UltrasonicSensor(Sensors.FRONT_RIGHT, 20, 21),
            CompassAdapter(Sensors.COMPASS, instrument_factory.get_compass()),
            InclinometerAdapter(Sensors.INCLINOMETER, instrument_factory.get_inclinometer())
        )


class InstrumentsFactory(object):
    SENSOR = False

    def call_sensor(self):
        if not self.SENSOR:
            self.SENSOR = LSM303()
            self.SENSOR.set_mag_gain(Adafruit_LSM303.LSM303_MAGGAIN_4_7)
        return self.SENSOR

    def get_inclinometer(self):
        return Inclinometer(self.call_sensor())

    def get_compass(self):
        return Compass(self.call_sensor())


class InclinometerAdapter(object):
    def __init__(self, sensor_key, inclinometer):
        """
        :type inclinometer: Inclinometer
        """
        self.SENSOR_KEY = sensor_key
        self.inclinometer = inclinometer

    def make_measurement(self):
        self.inclinometer.get_inclination()


class CompassAdapter(object):
    def __init__(self, sensor_key, compass):
        """
        :type compass: Compass
        """
        self.SENSOR_KEY = sensor_key
        self.compass = compass

    def make_measurement(self):
        return self.compass.get_heading()
