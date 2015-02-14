__author__ = 'nikolojedison'
from .set_claw_setpoint import SetClawSetpoint
import setpoints

class OpenClaw(SetClawSetpoint):
    """Opens the claw"""

    def __init__(self, robot):
        super().__init__(robot, setpoints.kOpen)
    def isFinished(self):
        """Current sensor stops the things if it gets trippin'."""
        return super().isFinished() or self.robot.claw.current.getVoltage() > setpoints.kStall
