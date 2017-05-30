from threading import Thread

import time


class ServiceThread(Thread):
    def __init__(self, flag, queue_in, queue_out, freq=0.1):
        super(ServiceThread, self).__init__()
        self.flag = flag
        self.flag.set()
        self.queue_in = queue_in
        self.queue_out = queue_out
        self.freq = freq

    def run(self):
        while self.flag.is_set():
            self.process()
            time.sleep(self.freq)

    def process(self):
        pass

    def stop(self):
        self.flag.clear()

    def get_queue_in(self):
        return self.queue_in

    def get_queue_out(self):
        return self.queue_out

    def get_flag(self):
        return self.flag
