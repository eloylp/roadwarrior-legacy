import sys
from pydoc import locate


class RoadWarrior:
    def run(self):
        try:
            builder = locate('.'.join(['builder',
                                       str(sys.argv[1]).lower(),
                                       str(sys.argv[1]).lower().capitalize() + 'Builder'
                                       ]))()
            mediator = builder.build()
            mediator.run()
        except (IndexError, TypeError):
            print "Program identity not valid."


if __name__ == '__main__':
    roadWarrior = RoadWarrior()
    roadWarrior.run()
