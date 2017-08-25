# coding=utf-8

import inspect

import roadwarrior
from roadwarrior.device.engine.engine import EngineBuilder
from roadwarrior.device.sensor.sensor import SensorBuilder
from roadwarrior.device.engine.service import EngineService
from roadwarrior.device.sensor.service import SensorService
from roadwarrior.mediator.patrol import Patrol


class PatrolBuilder(object):
    def __init__(self):
        pass

    @staticmethod
    def build():
        motors = EngineBuilder().get_engines()
        sensors = SensorBuilder().get_sensors()

        movements = {}
        for movement in inspect.getmembers(roadwarrior.device.engine.move, predicate=inspect.isclass):
            movements[movement[0]] = movement[1](motors)
        engine_service = EngineService(movements)

        sensors_service = SensorService(sensors)
        patrol = Patrol(sensors_service, engine_service)

        return patrol
