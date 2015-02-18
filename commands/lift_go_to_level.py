__author__ = 'nikolojedison'

from commands.set_lift_setpoint import SetLiftSetpoint
import setpoints

class LiftGoToLevel(SetLiftSetpoint):
    """This needs testing & the setpoints need to be properly set."""

    def __init__(self, robot, level, shift_up, shift_down):
        super().__init__(robot, setpoints.lift_level_setpoints[level])
