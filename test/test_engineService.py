# coding=utf-8

from unittest import TestCase
from mock import Mock
from roadwarrior.device.engine.service import EngineService


class TestEngineService(TestCase):
    def setUp(self):
        self.move1 = Mock()
        self.move2 = Mock()
        moves = {

            "MOVE1": self.move1,
            "MOVE2": self.move2
        }

        self.sut = EngineService(moves)

    def test_process_without_args(self):
        self.sut.process(("MOVE1",))
        self.move1.execute.assert_called()
        self.move2.execute.assert_not_called()

    def test_process_with_args(self):
        self.sut.process(("MOVE1", (1, 2)))
        self.move1.execute.assert_called_with(1, 2)
        self.move2.execute.assert_not_called()
