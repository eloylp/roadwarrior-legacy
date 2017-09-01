# coding=utf-8

from device.engine.move import AllStopMove, AllForwardMove, AllBackwardMove, TurnDegreesMove
from roadwarrior.behaviour.patrol import Patrol
from roadwarrior.device.engine.engine import EngineFactory
from roadwarrior.device.engine.navigation import TargetHeadingCalculator
from roadwarrior.device.engine.service import EngineService
from roadwarrior.device.sensor.definition import Sensors
from roadwarrior.device.sensor.sensor import SensorFactory
from roadwarrior.device.sensor.service import SensorService


class PatrolFactory(object):
    def __init__(self):
        pass

    @staticmethod
    def build():

        engines = EngineFactory().get_engines()
        sensors = SensorFactory().get_sensors()

        sensors_service = SensorService(sensors)

        movements = {

            AllStopMove.__name__: AllStopMove(engines),
            AllForwardMove.__name__: AllForwardMove(engines),
            AllBackwardMove.__name__: AllBackwardMove(engines),
            TurnDegreesMove.__name__: TurnDegreesMove(engines, sensors_service.get_sensor_by_key(Sensors.COMPASS),
                                                      TargetHeadingCalculator()),
        }

        engine_service = EngineService(movements)

        patrol = Patrol(sensors_service, engine_service)

        return patrol
