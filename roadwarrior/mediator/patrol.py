
import time


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

        while self.running:

            try:

                sensors_snapshot = self.sensors_queue.get(True)
                print sensors_snapshot
                if sensors_snapshot[0][1] > 30:
                    self.engine_queue.put("FORWARD")
                else:
                    self.engine_queue.put("STOP")

            except KeyboardInterrupt:
                self.engine_queue.put("STOP")
                time.sleep(2)
                self.sensors_service.get_flag().clear()
                self.engine_service.get_flag().clear()
                self.running = False
