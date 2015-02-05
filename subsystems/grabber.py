__author__ = 'nikolojedison'
import wpilib
from wpilib.command import PIDSubsystem

class Grabber(PIDSubsystem):

    def __init__(self, robot):
        super().__init__(1, 0, 0)
        self.robot = robot

        self.grabba_pot = wpilib.AnalogPotentiometer(1)
        self.motor = wpilib.Jaguar(4)
        self.current = wpilib.AnalogInput(3)
        self.setAbsoluteTolerance(.01)

    def initDefaultCommand(self):
        pass

    def log(self):
        wpilib.SmartDashboard.putData("Grabberness", self.grabba_pot) #publishes to the Dash
        wpilib.SmartDashboard.putData("Current Current", self.current)

    def returnPIDInput(self):
        return self.grabba_pot.get()

    def usePIDOutput(self, output):
        self.motor.set(output)
