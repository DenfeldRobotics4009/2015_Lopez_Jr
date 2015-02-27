__author__ = "nikolojedison"
import wpilib
from wpilib.command import Subsystem
import setpoints
from commands.manual_winch import ManualWinch

class Winch(Subsystem):
    """Runs the winch added at the LSR."""

    def __init__(self, robot):
        super().__init__()

        self.robot = robot
        self.motor = wpilib.Jaguar(0)

    def initDefaultCommand(self):
        self.setDefaultCommand(ManualWinch(self.robot))

    def manualSet(self, output):
        self.motor.set(output)

    def log(self):
        pass

