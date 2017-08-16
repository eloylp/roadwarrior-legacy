# coding=utf-8

from roadwarrior.device.engine.move import Descriptor


class EngineService(object):
    def __init__(self, move):
        self.move = move

    def process(self, command):
        if command[0] in Descriptor.__dict__.keys():
            self.move[command[0]].execute(*command[1])
