__author__ = 'nikolojedison'

from commands.set_lift_setpoint import SetLiftSetpoint

class LiftGoToLevel(SetLiftSetpoint):
    lift_level_setpoints = [.865, .7, .6, .5, .4, .3, .251] #bottom to top
    def __init__(self, robot, level):
        if self.lift_level_setpoints[level] == self.lift_level_setpoints[-1] and robot.mast.isBack():
            #If the lift is trying to go to the top and the mast is back:
            self.cancel()
            #Don't
        super().__init__(robot, self.lift_level_setpoints[level])
