__author__ = 'nikolojedison'
from .set_grabba_setpoint import SetGrabbaSetpoint

class GrabTote(SetGrabbaSetpoint):
    kCloseSetpoint = .425
    kStallPoint = 2
    def __init__(self, robot):
        super().__init__(robot, self.kCloseSetpoint)

    def isFinished(self):
        #Finishes the command if it reaches the setpoint or current draw is above kStallPoint.
        return super().isFinished() or self.robot.grabber.current.getVoltage() > self.kStallPoint
