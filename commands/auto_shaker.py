__author__ = 'nikolojedison'
#Hacked together from shaker.py's Shaker.
from wpilib.command import Command

from .drive_straight import DriveStraight
from .grab_tote import GrabTote

class AutoShaker(Command):
    """This is the simple auton."""
    def __init__(self, robot):
        super().__init__()
        self.grab_command = GrabTote(robot)
        self.drive_left = DriveStraight(robot, .25, 0, timeout=.25)
        self.drive_right = DriveStraight(robot, -.25, 0, timeout=.25)
        self.driving_right = True

    def initialize(self):
        self.grab_command.start()
        self.drive_right.start()

    def execute(self):
        self.grab_command
        self.drive_left()
        self.drive_right()
        super().execute()

    def cancel(self):
        self.grab_command.cancel()
        self.drive_left.cancel()
        self.drive_right.cancel()
        super().cancel()

    def isFinished(self):
        return False
