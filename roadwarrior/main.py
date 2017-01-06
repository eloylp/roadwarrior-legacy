import sys
from pydoc import locate


class RoadWarrior:
    def run(self):
        try:
            builder = locate('.'.join(['builders',
                                       str(sys.argv[1]).lower(),
                                       str(sys.argv[1]).lower().capitalize() + 'Builder'
                                       ]))()
            mediator = builder.build()
            mediator.run()
        except (IndexError, TypeError):
            print "Not identified program"


if __name__ == '__main__':
    roadWarrior = RoadWarrior()
    roadWarrior.run()
