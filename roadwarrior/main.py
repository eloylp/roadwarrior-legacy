# coding=utf-8

from __future__ import print_function
import sys
from pydoc import locate


class RoadWarrior(object):
    def __init__(self):
        pass

    def run(self):
        try:
            builder = locate('.'.join(['builder',
                                       str(sys.argv[1]).lower(),
                                       str(sys.argv[1]).lower().capitalize() + 'Builder'
                                       ]))
            mediator = builder.build()
            mediator.start()
        except (IndexError, TypeError):
            print("Program identity not valid.")


if __name__ == '__main__':
    roadWarrior = RoadWarrior()
    roadWarrior.run()
