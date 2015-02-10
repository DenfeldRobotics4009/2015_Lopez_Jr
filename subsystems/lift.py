__author__ = 'nikolojedison'
import wpilib
from wpilib.command import PIDSubsystem

class Lift(PIDSubsystem):
    kUp = .240
    kTop = .251
    kBottom = .865

    def __init__(self, robot):
        super().__init__(1, 0, 0)
        self.robot = robot

        self.lift_pot = wpilib.AnalogPotentiometer(1)
        self.motor = wpilib.CANTalon(0)
        self.setAbsoluteTolerance(.01)

    def initDefaultCommand(self):
        pass

    def manualSet(self, output):
        position = self.lift_pot.get()
        if position > self.kBottom and output < 0:
            self.motor.set(0)
        elif position < self.kTop and output > 0:
            self.motor.set(0)
        else:
            self.motor.set(output)

    def log(self):
        wpilib.SmartDashboard.putNumber("Elevator Pot", self.lift_pot.get()) #publishes to the Dash

    def returnPIDInput(self):
        return self.lift_pot.get()

    def usePIDOutput(self, output):
        self.motor.set(output)

    def isUp(self):
        """If the lift is all the way up..."""
        self.lift_pot.get() > self.kUp
