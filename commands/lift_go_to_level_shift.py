__author__ = 'nikolojedison'

from wpilib.command import Command
import setpoints

class LiftGoToLevelShift(Command):
    """This is the shifting stuff. Useful."""
    def __init__(self, robot, level, top_shift, bottom_shift):
        super().__init__()
        self.robot = robot
        self.setTimeout(5)
        self.level = level
        self.shift_up_button = top_shift
        self.shift_down_button = bottom_shift
        self.requires(self.robot.lift)

    def initialize(self):
        self.robot.lift.enable()
        if self.shift_up_button.get():
            self.robot.lift.setSetpoint(setpoints.lift_step_setpoints[self.level])
        elif self.shift_down_button.get():
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
