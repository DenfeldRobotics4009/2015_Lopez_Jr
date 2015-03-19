__author__ = "nikolojedison"
from wpilib.command import Command
from drive_control import dead_zone

class DefaultLock(Command):
    """Manually runs the lock."""
    def __init__(self, robot):
        super().__init__()
        self.robot = robot
        self.requires(self.robot.lock)


    def execute(self):
        self.robot.lock.manualSet(True)

    def isFinished(self):
        return False

    def cancel(self):
        super().cancel()
