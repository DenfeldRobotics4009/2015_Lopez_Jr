__author__ = "nikolojedison"
from wpilib.command import Command
from subsystems.winch import Winch

class WinchButton(Command):
    def __init__(self, robot, speed):
        super().__init__()
        self.robot = robot
        self.requires(self.robot.winch)
        self.speed = speed

    def execute(self):
        self.robot.winch.manualSet(self.speed)

    def isFinished(self):
        return False

    def end(self):
        self.robot.winch.manualSet(0)

    def cancel(self):
        self.end()
        super().cancel()
