__author__ = 'nikolojedison'
from .set_mast_setpoint import SetMastSetpoint
import setpoints

class MastLevel(SetMastSetpoint):
    """Moves the mast so that the forks are parallel with the ground."""

    def __init__(self, robot):
        """Cannot stop the things in Autonomous. DO NOT make it cancel in auto."""
        if robot.lift.isUp(): #If the lift is up:
            self.cancel() #Stop the mast tiltery

        super().__init__(robot, setpoints.kMastParallel)

