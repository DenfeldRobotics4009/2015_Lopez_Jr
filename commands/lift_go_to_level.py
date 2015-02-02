__author__ = 'nikolojedison'

from commands.set_lift_setpoint import SetLiftSetpoint

class LiftGoToLevel(SetLiftSetpoint):
    lift_level_setpoints = [] #bottom to top
    def __init__(self, robot, level):
        if LiftLevelSetpoints[level] == lift_level_setpoints[-1] and robot.mast.isBack():
            #If the lift is trying to go to the top and the mast is back:
            self.cancel()
            #Don't
        super.__init__(robot, lift_level_setpoints[level])