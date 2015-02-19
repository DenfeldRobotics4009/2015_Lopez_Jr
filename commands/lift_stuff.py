__author__ = "nikolojedison"
from wpilib.command import Command
from subsystems.lift import Lift

class LiftStuff(Command):
    def __init__(self, robot, speed, timeout):
        super().__init__()
        self.robot = robot
        self.requires(self.robot.lift)
        self.speed = speed
        self.setTimeout(timeout)

    def execute(self):
        self.robot.lift.manualSet(self.speed)

    def isFinished(self):
        return self.isTimedOut()

    def end(self):
        self.robot.lift.manualSet(0)

    def cancel(self):
        self.end()
        super().cancel()
