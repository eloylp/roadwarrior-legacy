# coding=utf-8

import inspect

import roadwarrior
from roadwarrior.device.engine.navigation import TargetHeadingCalculator
from roadwarrior.device.sensor.definition import Sensors
from roadwarrior.device.engine.engine import EngineFactory
from roadwarrior.device.sensor.sensor import SensorFactory
from roadwarrior.device.engine.service import EngineService
from roadwarrior.device.sensor.service import SensorService
from roadwarrior.behaviour.patrol import Patrol


class PatrolFactory(object):
    def __init__(self):
        pass

    @staticmethod
    def build():

        engines = EngineFactory().get_engines()
        sensors = SensorFactory().get_sensors()

        sensors_service = SensorService(sensors)

        movements = {}
        for movement in inspect.getmembers(roadwarrior.device.engine.move, predicate=inspect.isclass):
            if 'Turn' in movement[0]:
                movements[movement[0]] = movement[1](
                    engines,
                    sensors_service.get_sensor_by_key(Sensors.COMPASS),
                    TargetHeadingCalculator()
                )
        engine_service = EngineService(movements)

        patrol = Patrol(sensors_service, engine_service)

        return patrol
