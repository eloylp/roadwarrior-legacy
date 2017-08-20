# coding=utf-8

from __future__ import print_function

from device.sensor.definition import Sensors
from roadwarrior.device.engine.move import AllForwardMove, AllStopMove, TurnDegreesMove


class Patrol(object):
    def __init__(self, sensors_service, engine_service):

        """
        :type sensors_service: roadwarrior.device.sensor.service.UltrasonicSensorService
        :type engine_service: roadwarrior.device.engine.service.EngineService
        """
        self.sensors_service = sensors_service
        self.engine_service = engine_service
        self.running = True

    def start(self):

        self.running = True
        self.run()

    def stop(self):
        self.running = False

    def run(self):

        self.engine_service.process((AllStopMove.__name__,))

        while self.running:
            try:
                self.make_step()
            except KeyboardInterrupt:
                self.running = False
        self.engine_service.process((AllStopMove.__name__,))

    def make_step(self):
        total_front_sensors = 0
        count = 0
        for sensor, measurement in self.sensors_service.process().__dict__.items():
            if sensor.upper() in [Sensors.FRONT_FRONT, Sensors.FRONT_LEFT, Sensors.FRONT_RIGHT]:
                total_front_sensors += measurement
                count += 1
        if count:
            if total_front_sensors / count <= 10:
                self.engine_service.process((AllStopMove.__name__,))
                self.engine_service.process((TurnDegreesMove.__name__, (60,)))
        self.engine_service.process((AllForwardMove.__name__, (60,)))
