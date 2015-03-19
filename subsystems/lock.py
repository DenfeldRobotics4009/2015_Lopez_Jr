__author__ = "nikolojedison"
import wpilib
from wpilib.command import Subsystem
import setpoints
from commands.default_lock import DefaultLock

class Lock(Subsystem):
    """Runs the lock."""

    def __init__(self, robot):
        super().__init__()

        self.robot = robot
        self.spike = wpilib.Relay(1)

    def initDefaultCommand(self):
        self.setDefaultCommand(DefaultLock(self.robot))

    def manualSet(self, output):
        if output:
            self.spike.set(self.spike.Value.kReverse)
        else:
            self.spike.set(self.spike.Value.kOn)

    def log(self):
        pass

