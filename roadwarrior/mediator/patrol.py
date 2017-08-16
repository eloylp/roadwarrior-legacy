# coding=utf-8

from __future__ import print_function
import time


class Patrol(object):
    def __init__(self, engine_service, sensors_service):

        """
        :type engine_service: roadwarrior.device.engine.service.EngineService
        :type sensors_service: roadwarrior.device.sensor.service.UltrasonicSensorService
        """
        self.engine_service = engine_service
        self.sensors_service = sensors_service

        self.running = True

    def run(self):

        while self.running:
            try:

                for k, v in self.sensors_service.process().__dict__.items():
                    if v is not False and v < 20:
                        print(v)
                        time.sleep(2)
                        break

            except KeyboardInterrupt:
                time.sleep(2)
                self.running = False
