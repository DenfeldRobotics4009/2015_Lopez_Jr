__author__ = 'nikolojedison'
from .set_grabba_setpoint import SetGrabbaSetpoint

class OpenGrabba(SetGrabbaSetpoint):
    kOpenSetpoint = .118
    kStallPoint = 2
    def __init__(self, robot):
        super().__init__(robot, self.kOpenSetpoint)

    def isFinished(self):
        return super().isFinished() or self.robot.grabber.current.getVoltage() > self.kStallPoint
