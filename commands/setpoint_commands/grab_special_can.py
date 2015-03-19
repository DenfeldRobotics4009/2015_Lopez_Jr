__author__ = "nikolojedison"
from commands.set_claw_setpoint import SetClawSetpoint
import setpoints

class GrabSpecialCan(SetClawSetpoint):
    """This is the basic can grabbing stuff."""

    def __init__(self, robot):
        super().__init__(robot, setpoints.kSpecialCan)

    def isFinished(self):
        return super().isFinished() or self.robot.claw.current.getVoltage() > setpoints.kStall
