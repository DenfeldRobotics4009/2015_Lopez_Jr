__author__ = 'nikolojedison'
from set_mast_setpoint import SetMastSetpoint

class MastBack(SetMastSetpoint):
    kBackSetpoint = 1

    def __init__(self, robot):
        """Cannot stop the things in Autonomous. DO NOT make it cancel in auto."""
        if robot.lift.isUp(): #If the lift is up:
            self.cancel() #Stop the mast tiltery

        super.__init__(robot, kBackSetpoint)

