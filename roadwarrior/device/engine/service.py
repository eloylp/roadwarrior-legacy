from Queue import Empty

from device.engine.move import Descriptor
from roadwarrior.device.base import ServiceThread


class EngineService(ServiceThread):
    def __init__(self, flag, queue_in, move):

        super(EngineService, self).__init__(flag, queue_in, False)
        self.move = move

    def process(self):

        try:

            command = self.queue_in.get(False)

            if command[0] in Descriptor.__dict__.keys():
                self.move[command[0]].execute(*command[1])
        except Empty:
            pass
