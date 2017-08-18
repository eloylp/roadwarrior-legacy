# coding=utf-8

class EngineService(object):
    def __init__(self, move):
        self.move = move

    def process(self, command):
        if command[0] in self.move.keys():
            self.move[command[0]].execute(*command[1])
