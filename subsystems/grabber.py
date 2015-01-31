__author__ = 'nikolojedison'
from wpilib.command import PIDSubsystem

class Grabber(PIDSubsystem):

    def __init__(self, robot)
        super().__init__()
        self.robot = robot
        self.grabba_pot = wpilib.AnalogPotentiometer(1)

    def initDefaultCommand(self):
        pass
