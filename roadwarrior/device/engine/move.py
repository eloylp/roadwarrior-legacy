# coding=utf-8


from device.engine.definition import Direction, EngineLocation


class AllStopMove(object):
    def __init__(self, engines):
        self.engines = engines

    def execute(self):
        for e in self.engines:
            e.motor.brake()
            e.motor.release()


class AllForwardMove(object):
    def __init__(self, engines):
        self.engines = engines

    def execute(self, speed):
        for e in self.engines:
            e.motor.set_speed(speed)
            e.motor.advance_forward()


class AllBackwardMove(object):
    def __init__(self, engines):
        self.engines = engines

    def execute(self, speed):
        for e in self.engines:
            e.motor.set_speed(speed)
            e.motor.advance_backward()


class TurnDegreesMove(object):
    def __init__(self, engines, heading_sensor, heading_target_calculator):
        """
        :type engines: roadwarrior.device.engine.engine.Engine[]
        :type sensor_service: roadwarrior.device.sensor.service.SensorService
        :type heading_target_calculator: roadwarrior.device.engine.navigation.TargetHeadingCalculator

        """
        self.engines = engines
        self.heading_sensor = heading_sensor
        self.heading_target_calculator = heading_target_calculator
        self.__prepare_engines()

    def __prepare_engines(self):

        self.motor_back_left = self.__engine_selector(EngineLocation.BACK_LEFT)
        self.motor_front_left = self.__engine_selector(EngineLocation.FRONT_LEFT)

        self.motor_back_right = self.__engine_selector(EngineLocation.BACK_RIGHT)
        self.motor_front_right = self.__engine_selector(EngineLocation.FRONT_RIGHT)

        self.prepared_engines = [
            self.motor_back_left,
            self.motor_front_left,
            self.motor_back_right,
            self.motor_front_right
        ]

    def execute(self, direction, degrees, speed=40):

        actual_degrees = self.heading_sensor.make_measurement()

        for engine in self.prepared_engines:
            engine.motor.set_speed(speed)

        if direction == Direction.RIGHT:
            forward_engines = [self.motor_front_left, self.motor_back_left]
            backward_engines = [self.motor_front_right, self.motor_back_right]
        elif direction == Direction.LEFT:
            forward_engines = [self.motor_front_right, self.motor_back_right]
            backward_engines = [self.motor_front_left, self.motor_back_left]
        else:
            raise KeyError

        for forward_engine in forward_engines:
            forward_engine.motor.advance_forward()
        for backward_engine in backward_engines:
            backward_engine.motor.advance_backward()

        target_degrees = self.heading_target_calculator.calculate(actual_degrees, degrees, direction)

        while self.heading_sensor.make_measurement() != target_degrees:
            pass

        for engine in self.prepared_engines:
            engine.motor.brake()
            engine.motor.release()

    def __engine_selector(self, engine_key):

        for engine in self.engines:
            if engine.engine_key is engine_key:
                return engine
        raise KeyError
