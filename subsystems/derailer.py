__author__ = 'nikolojedison'
from wpilib.command import Subsystem
from commands.derailer_go import DerailerGo
import wpilib

class Derailer(Subsystem):

    def __init__(self, robot):
        self.robot = robot
        self.motor = wpilib.Jaguar(4)

    def initDefaultCommand(self):
        self.setDefaultCommand(DerailerGo(self.robot))

    def log(self):
        pass

    def set(output):
        self.motor.set(output)
