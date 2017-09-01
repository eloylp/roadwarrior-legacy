# coding=utf-8


class TargetHeadingCalculator(object):
    def __init__(self, precision=1):

        self.precision = precision

    def calculate(self, actual_heading_degrees, desired_heading_degrees, direction):

        desired_heading_degrees = self.__reduce_over_loop(desired_heading_degrees)

        if direction == Direction.RIGHT:
            result = self.__calculate_to_right(actual_heading_degrees, desired_heading_degrees)
        elif direction == Direction.LEFT:
            result = self.__calculate_to_left(actual_heading_degrees, desired_heading_degrees)
        else:
            raise KeyError

        return self.__adjust_precision(result)

    def __calculate_to_right(self, actual_heading_degrees, desired_heading_degrees):
        if actual_heading_degrees + desired_heading_degrees > 360:
            return (actual_heading_degrees + desired_heading_degrees) - 360
        else:
            return actual_heading_degrees + desired_heading_degrees

    def __calculate_to_left(self, actual_heading_degrees, desired_heading_degrees):
        if actual_heading_degrees - desired_heading_degrees < 0:
            return 360 + (actual_heading_degrees - desired_heading_degrees)
        else:
            return actual_heading_degrees - desired_heading_degrees

    def __adjust_precision(self, value):

        return round(value, self.precision)

    def __reduce_over_loop(self, desired_heading_degrees):

        if desired_heading_degrees > 360:
            desired_heading_degrees %= 360
        return desired_heading_degrees


class Direction(object):
    LEFT = 'LEFT'
    RIGHT = 'RIGHT'