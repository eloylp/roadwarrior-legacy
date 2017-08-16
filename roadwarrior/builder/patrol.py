# coding=utf-8

from roadwarrior.device.engine.engine import EngineBuilder
from roadwarrior.device.engine.move import AllForwardMove, AllBackwardMove, Descriptor, AllStopMove, TurnDegreesMove
from roadwarrior.device.sensor.sensor import UltrasonicSensorBuilder
from roadwarrior.device.engine.service import EngineService
from roadwarrior.device.sensor.service import UltrasonicSensorService
from roadwarrior.mediator.patrol import Patrol


class PatrolBuilder(object):
    def __init__(self):
        pass

    @staticmethod
    def build():
        motors = EngineBuilder().get_engines()
        sensors = UltrasonicSensorBuilder().get_ultrasonic_sensors()

        engine_service = EngineService(
            {
                Descriptor.FORWARD: AllForwardMove(motors),
                Descriptor.BACKWARD: AllBackwardMove(motors),
                Descriptor.TURN: TurnDegreesMove(motors),
                Descriptor.STOP: AllStopMove(motors)

            })
        sensors_service = UltrasonicSensorService(sensors)
        patrol = Patrol(engine_service, sensors_service)

        return patrol
