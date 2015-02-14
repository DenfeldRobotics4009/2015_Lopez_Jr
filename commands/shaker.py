__author__ = 'nikolojedison'

from wpilib.command import CommandGroup

from .drive_straight import DriveStraight
from .grab_tote import GrabTote

class Shaker(CommandGroup):
    """This is the simple auton."""
    def __init__(self, robot):
        super().__init__()
        self.grab_command = GrabTote(robot)
        self.addParallel(self.grab_command)
        self.shakers_generator = [
            DriveStraight(robot, .25, 0, timeout=.2),
            DriveStraight(robot, -.25, 0, timeout=.2),
            DriveStraight(robot, .25, 0, timeout=.2),
            DriveStraight(robot, -.25, 0, timeout=.2),
            DriveStraight(robot, .25, 0, timeout=.2),
            DriveStraight(robot, -.25, 0, timeout=.2),
            DriveStraight(robot, .25, 0, timeout=.2),
            DriveStraight(robot, -.25, 0, timeout=.2)]

        for i in self.shakers_generator: self.addSequential(i)

    def cancel(self):
        self.grab_command._cancel()
        self.grab_command.end()
        for i in self.shakers_generator:
            i._cancel()
            i.end()
        super().cancel()
