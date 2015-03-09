__author__ = 'nikolojedison'
from .commands.set_mast_setpoint import SetMastSetpoint
import setpoints

class MastForward(SetMastSetpoint):
    """Sends the mast forward"""

    def __init__(self, robot):
        super().__init__(robot, setpoints.kMastForwardLimit)

