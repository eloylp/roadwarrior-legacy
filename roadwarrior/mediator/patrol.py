import time

from device.engine.move import Descriptor


class Patrol:
    def __init__(self, engine_service, sensors_service):

        """
        :type engine_service: roadwarrior.device.engine.service.EngineService
        :type sensors_service: roadwarrior.device.sensor.service.UltrasonicSensorService
        """
        self.engine_service = engine_service
        self.sensors_service = sensors_service

        self.sensors_service.start()
        self.engine_service.start()

        self.sensors_queue = self.sensors_service.get_queue_out()
        self.engine_queue = self.engine_service.get_queue_in()
        self.running = True

    def run(self):

        self.engine_queue.put((Descriptor.FORWARD, (30,)))

        while self.running:
            try:
                sensors_snapshot = self.sensors_queue.get(True)

                for k, v in sensors_snapshot.__dict__.items():
                    if v is not False and v < 20:
                        print v
                        self.engine_queue.put((Descriptor.TURN, (60, 45)))
                        time.sleep(2)
                        self.engine_queue.put((Descriptor.FORWARD, (30,)))
                        self.sensors_queue.queue.clear()
                        break

            except KeyboardInterrupt:
                self.engine_queue.put((Descriptor.STOP, ()))
                time.sleep(2)
                self.sensors_service.get_flag().clear()
                self.engine_service.get_flag().clear()
                self.running = False
