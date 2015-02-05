__author__ = 'nikolojedison'
from .set_grabba_setpoint import SetGrabbaSetpoint

class OpenGrabba(SetGrabbaSetpoint):
    kOpenSetpoint = .9
    kStallPoint = 1.1
    def __init__(self, robot):
        super().__init__(robot, self.kOpenSetpoint)

    def isFinished(self):
        super.isFinished() or self.robot.grabber.current.getVoltage() > self.kStallPoint
