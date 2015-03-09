__author__ = 'nikolojedison'
from commands.set_claw_setpoint import SetClawSetpoint
import setpoints

class CloseClaw(SetClawSetpoint):
    """Closes the claw."""
    def __init__(self, robot):
        super().__init__(robot, setpoints.kClose)

    def isFinished(self):
        #Finishes the command if it reaches the setpoint or current draw is above kStallPoint.
        return super().isFinished() or self.robot.claw.current.getVoltage() > setpoints.kStall
