# coding=utf-8

from __future__ import print_function

from roadwarrior.device.engine.move import AllForwardMove


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

    def make_step(self):
        for sensor, measurement in self.sensors_service.process().__dict__.items():
            pass

        self.engine_service.process((AllForwardMove.__name__, 23))

    def run(self):

        while self.running:
            try:
                self.make_step()
            except KeyboardInterrupt:
                self.running = False
