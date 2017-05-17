from threading import Thread


class Patrol(Thread):
    def __init__(self, communications_service, engine_service, sensors_service):
        """
        :type communications_service: services.communications.service.CommunicationsService
        :type engine_service: services.engine.service.EngineService
        :type sensors_service: services.sensors.service.SensorsService
        """
        super(Patrol, self).__init__()
        self.communications_service = communications_service
        self.engine_service = engine_service
        self.sensors_service = sensors_service

    def run(self):
        # TODO implement mediation between sevices.


        pass
