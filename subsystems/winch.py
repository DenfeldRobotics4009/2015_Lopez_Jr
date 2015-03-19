__author__ = "nikolojedison"
import wpilib
from wpilib.command import Subsystem
import setpoints
from commands.manual_commands.manual_winch import ManualWinch

class Winch(Subsystem):
    """Runs the winch."""

    def __init__(self, robot):
        super().__init__()

        self.robot = robot
        self.motor = wpilib.Jaguar(4)

    def initDefaultCommand(self):
        self.setDefaultCommand(ManualWinch(self.robot))

    def manualSet(self, output):
        self.motor.set(output*.85)

    def log(self):
        pass

