__author__ = 'nikolojedison'

from commands.set_lift_setpoint import SetLiftSetpoint
import setpoints

class LiftGoToLevel(SetLiftSetpoint):
    """This needs testing & the setpoints need to be properly set."""

    def __init__(self, robot, level):
        if setpoints.lift_level_setpoints[level] == setpoints.lift_level_setpoints[-1] and robot.mast.isBack():
            #If the lift is trying to go to the top and the mast is back:
            self.cancel()
            #Don't
        super().__init__(robot, setpoints.lift_level_setpoints[level])
