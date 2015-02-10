__author__ = 'nikolojedison'
from .set_claw_setpoint import SetClawSetpoint

class OpenClaw(SetClawSetpoint):
    kOpenSetpoint = .118
    kStallPoint = 2
    def __init__(self, robot):
        super().__init__(robot, self.kOpenSetpoint)

    def isFinished(self):
        return super().isFinished() or self.robot.claw.current.getVoltage() > self.kStallPoint
