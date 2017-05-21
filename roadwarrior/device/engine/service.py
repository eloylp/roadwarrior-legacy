from Queue import Empty

from roadwarrior.device.base import ServiceThread


class EngineService(ServiceThread):
    def __init__(self, flag, queue_in, motors, freq=0.5):

        super(EngineService, self).__init__(flag, queue_in, False, freq)
        self.motors = motors

    def process(self):

        try:

            command = self.queue_in.get(False)

            if command == "FORWARD":
                for motor in self.motors:
                    motor.set_speed(30)
                    motor.advance_forward()

            if command == "STOP":
                for motor in self.motors:
                    motor.brake()
                    motor.release()
        except Empty:
            pass
