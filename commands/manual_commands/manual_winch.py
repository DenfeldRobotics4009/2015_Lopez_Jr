__author__ = "nikolojedison"
from wpilib.command import Command
from drive_control import dead_zone

class ManualWinch(Command):
    """Manually runs the winch."""
    def __init__(self, robot):
        super().__init__()
        self.robot = robot
        self.requires(self.robot.winch)

    def execute(self):
        self.robot.winch.manualSet(dead_zone(self.robot.oi.getPad().getX(self), .25))

    def isFinished(self):
        return False

    def cancel(self):
        self.robot.winch.manualSet(0)
        super().cancel()
