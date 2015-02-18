__author__ = 'nikolojedison'

from wpilib.command import Command
import setpoints

class LiftGoToLevelShift(Command):

    def __init__(self, robot, level, shift_up_button, shift_down_button):
        super().__init__()
        self.robot = robot
        self.setTimeout(5)
        self.level = level
        self.shift_up_button = shift_up_button
        self.shift_down_button = shift_down_button
        self.requires(self.robot.lift)

    def initialize(self):
        self.robot.lift.enable()
        if shift_up_button.get():
            self.robot.lift.setSetpoint(setpoints.lift_step_setpoints[self.level])
        elif shift_down_button.get():
            self.robot.lift.setSetpoint(setpoints.lift_drop_setpoints[self.level])
        else:
            self.robot.lift.setSetpoint(setpoints.lift_level_setpoints[self.level])

    def isFinished(self):
        return self.robot.lift.onTarget() or self.isTimedOut() #Stay on target...

    def end(self):
        self.robot.lift.disable()

    def interupted(self):
        self.end()

    def cancel(self):
        self.end()
        super().cancel()
