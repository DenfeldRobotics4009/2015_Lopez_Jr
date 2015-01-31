__author__ = 'nikolojedison'
from wpilib.command import PIDSubsystem

class Lift(PIDSubsystem):

    def __init__(self, robot)
        super().__init__()
        self.robot = robot
        self.lift_pot = wpilib.AnalogPotentiometer(2)

    def initDefaultCommand(self):
        pass
