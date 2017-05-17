from Queue import Queue
from threading import Event

from mediator.patrol import Patrol
from device.communication.service import CommunicationsService
from device.engine.service import EngineService
from device.sensor.service import SensorsService


class PatrolBuilder:
    def build(self):
        com_flag = Event()
        com_queue_in = Queue()
        com_queue_out = Queue()

        eng_flag = Event()
        eng_queue_in = Queue()
        eng_queue_out = Queue()

        sens_flag = Event()
        sens_queue_in = Queue()
        sens_queue_out = Queue()

        communications_service = CommunicationsService(com_flag, com_queue_in, com_queue_out)
        engine_service = EngineService(eng_flag, eng_queue_in, eng_queue_out)
        sensors_service = SensorsService(sens_flag, sens_queue_in, sens_queue_out)
        patrol = Patrol(communications_service, engine_service, sensors_service)

        return patrol
