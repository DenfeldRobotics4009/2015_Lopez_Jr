__author__ = 'nikolojedison'
import .set_grabba_setpoint

class OpenGrabba(SetGrabbaSetpoint):
    kOpenSetpoint = .9
    def __init__(self, robot):
        super.__init__(robot, kOpenSetpoint)