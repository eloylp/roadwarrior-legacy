from threading import Thread


class Patrol(Thread):
    def __init__(self, engine_service, sensors_service):
        """
        :type engine_service: roadwarrior.device.engine.service.EngineService
        :type sensors_service: roadwarrior.device.sensor.service.UltrasonicSensorService
        """
        super(Patrol, self).__init__()
        self.engine_service = engine_service
        self.sensors_service = sensors_service

    def run(self):
        # TODO implement mediation between sevices.
        pass
