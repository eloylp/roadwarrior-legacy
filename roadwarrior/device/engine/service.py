# coding=utf-8


class EngineService(object):
    def __init__(self, movements):
        self.movements = movements

    def process(self, command):
        if command[0] in self.movements.keys():
            if len(command) is 2:
                self.movements[command[0]].execute(*command[1])
            else:
                self.movements[command[0]].execute()
