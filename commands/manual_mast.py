from wpilib.command import Command
from drive_control import dead_zone

class ManualMast(Command):
    def __init__(self, robot):
        super().__init__()
        self.robot = robot
        self.requires(self.robot.mast)

    def execute(self):
        self.robot.mast.manualSet(dead_zone(self.robot.oi.getJoystickLeft().getThrottle(), .1) * .33)

    def isFinished(self):
        return False

    def cancel(self):
        self.robot.mast.manualSet(0)
        super().cancel()
