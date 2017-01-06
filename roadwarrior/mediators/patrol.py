from threading import Thread


class Patrol(Thread):
    def __init__(self, communications_service, engine_service, sensors_service):
        super(Patrol, self).__init__()
        self.communications_service = communications_service
        self.engine_service = engine_service
        self.sensors_service = sensors_service

    def run(self):
        # TODO implement mediation between sevices.
        pass
