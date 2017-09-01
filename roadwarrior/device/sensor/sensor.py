# coding=utf-8

import time

import Adafruit_LSM303
from Adafruit_LSM303 import LSM303
from Adafruit_LSM303.instruments import Compass, Inclinometer
from RPi import GPIO

from roadwarrior.device.sensor.definition import Sensors


class InstrumentAdapterBase(object):
    def __init__(self, precision=1):

        self.precision = precision

    def adjust_precision(self, value):

        if type(value) in [int, float]:
            return self.__adjust_precision_from_value(value)
        elif type(value) in [list, tuple]:
            return self.__adjust_precision_from_iterable(value)
        else:
            raise TypeError

    def __adjust_precision_from_value(self, value):

        return round(value, self.precision)

    def __adjust_precision_from_iterable(self, iterable):
        value_list = []
        for value in iterable:
            value_list.append(round(value, self.precision))
        return tuple(value_list)



class UltrasonicSensor(InstrumentAdapterBase):
    def __init__(self, sensor_key, pin_trigger, pin_echo, precision=2):

        InstrumentAdapterBase.__init__(self, precision)

        self.sensor_key = sensor_key
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
        distance_cm = distance_meters * 100
        distance_cm = self.adjust_precision(distance_cm)
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


class InclinometerAdapter(InstrumentAdapterBase):
    def __init__(self, sensor_key, inclinometer, precision=1):
        """
        :type inclinometer: Inclinometer
        """
        InstrumentAdapterBase.__init__(self, precision)
        self.sensor_key = sensor_key
        self.inclinometer = inclinometer

    def make_measurement(self):
        measurement = self.inclinometer.get_inclination()
        return self.adjust_precision(measurement)


class CompassAdapter(InstrumentAdapterBase):
    def __init__(self, sensor_key, compass, precision=1):
        """
        :type compass: Compass
        """
        InstrumentAdapterBase.__init__(self, precision)
        self.sensor_key = sensor_key
        self.compass = compass

    def make_measurement(self):
        heading = self.compass.get_heading()
        return self.adjust_precision(heading)
