# coding=utf-8

from __future__ import print_function
import sys
from pydoc import locate


class RoadWarrior(object):
    def __init__(self):
        pass

    def run(self):
        try:
            factory = locate('.'.join(['factory',
                                       str(sys.argv[1]).lower(),
                                       str(sys.argv[1]).lower().capitalize() + 'Factory'
                                       ]))
            mediator = factory.build()
            mediator.start()
        except (IndexError, TypeError):
            print("Program identity not valid.")


if __name__ == '__main__':
    roadWarrior = RoadWarrior()
    roadWarrior.run()
