__author__ = 'nikolojedison'
import wpilib
from wpilib.command import PIDSubsystem

class Lift(PIDSubsystem):
    kUp = 4.5

    def __init__(self, robot)
        super().__init__(1, 0, 0)
        self.robot = robot

        self.lift_pot = wpilib.AnalogPotentiometer(2)
        self.motor = wpilib.Jaguar(6)

    def initDefaultCommand(self):
        pass

    def log(self):
        wpilib.SmartDashboard.putData("Lift level", self.lift_pot) #publishes to the Dash

    def returnPIDInput(self):
        return self.lift_pot.get()

    def usePIDOutput(self, output):
        self.motor.set(output)

    def isUp(self):
        """If the lift is all the way up..."""
        self.lift_pot.get() > self.kUp
