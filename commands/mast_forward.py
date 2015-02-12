__author__ = 'nikolojedison'
from .set_mast_setpoint import SetMastSetpoint

class MastForward(SetMastSetpoint):
    kForwardSetpoint = .65
    def __init__(self, robot):
        super().__init__(robot, robot.mast.kForwardLimit)

