from wpilib.command import Command
from subsystems.mast import Mast

class MastButton(Command):
    def __init__(self, robot, speed):
        super().__init__()
        self.robot = robot
        self.requires(self.robot.mast)
        self.speed = speed

    def execute(self):
        self.robot.mast.manualSet(self.speed)

    def isFinished(self):
        return False

    def end(self):
        self.robot.mast.manualSet(0)

    def cancel(self):
        self.end()
        super().cancel()
