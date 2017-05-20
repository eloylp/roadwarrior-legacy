from Queue import Queue
from threading import Event

from device.engine.engine import EngineBuilder
from device.sensor.sensor import UltrasonicSensorBuilder
from roadwarrior.device.engine.service import EngineService
from roadwarrior.device.sensor.service import UltrasonicSensorService
from roadwarrior.mediator.patrol import Patrol


class PatrolBuilder:
    def build(self):
        engine_flag = Event()
        engine_command_queue = Queue()

        sensor_flag = Event()
        sensor_queue_out = Queue()

        motors = EngineBuilder().get_engines()
        sensors = UltrasonicSensorBuilder().get_ultrasonic_sensors()

        engine_service = EngineService(engine_flag, engine_command_queue, motors)
        sensors_service = UltrasonicSensorService(sensor_flag, sensor_queue_out, sensors)
        patrol = Patrol(engine_service, sensors_service)

        return patrol
