__author__ = 'nikolojedison'

from wpilib.command import CommandGroup

from .commands.semiauto_commands.drive_straight import DriveStraight

class DriveAutonomous(CommandGroup):
    """This is the simple auton."""
    def __init__(self, robot):
        super().__init__()
        #simply drives for a bit. Might be our most valuable asset until we get our turning nailed down.
        self.auton_generator = [DriveStraight(robot, 0, -.5, timeout=5)]

        for i in self.auton_generator: self.addSequential(i)

    def cancel(self):
        for i in self.auton_generator: i._cancel()
        super().cancel()
