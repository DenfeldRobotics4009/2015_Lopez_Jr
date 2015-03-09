__author__ = 'nikolojedison'
from commands.set_claw_setpoint import SetClawSetpoint
import setpoints

class GrabSpecialTote(SetClawSetpoint):
    """Grabba da tote, man, usa da forks."""

    def __init__(self, robot):
        super().__init__(robot, setpoints.kSpecialTote)

    def isFinished(self):
        #Finishes the command if it reaches the setpoint or current draw is above kStallPoint.
        return super().isFinished() or self.robot.claw.current.getVoltage() > setpoints.kStall
