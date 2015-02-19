__author__ = 'auxiliary-character, nikolojedison'
from wpilib.command import Command
import wpilib

class TimedTurn(Command):
    """Drives the robot straight using the navX, PIDs, and a bit of math."""
    def __init__(self, robot, speed, timeout):
        super().__init__()
        self.robot = robot
        self.requires(self.robot.drivetrain)
        self.setTimeout(timeout)
        self.speed = speed

    def initialize(self):
        self.robot.drivetrain.driveManual(0, 0, speed)

    def isFinished(self):
        return self.isTimedOut()

    def end(self):
        self.robot.drivetrain.driveManual(0,0,0)

    def interupted(self):
        self.end()

    def _cancel(self):
        self.end()
        super()._cancel()
