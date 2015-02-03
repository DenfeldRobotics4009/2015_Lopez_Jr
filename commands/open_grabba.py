__author__ = 'nikolojedison'
import .set_grabba_setpoint

class OpenGrabba(SetGrabbaSetpoint):
    kOpenSetpoint = .9
    kStallPoint = 1.1
    def __init__(self, robot):
        super.__init__(robot, kOpenSetpoint)

    def isFinished():
        super.isFinished() or self.robot.grabber.current.getVoltage() > kStallPoint
