__author__ = 'nikolojedison'
import wpilib
from wpilib.command import PIDSubsystem

class Mast(PIDSubsystem):
    kBack = .50
    kBackLimit = .48
    kForwardLimit = .65

    def __init__(self, robot):
        super().__init__(40, 0, 0) #__init__(P, I, D)
        self.robot = robot

        self.mast_pot = wpilib.AnalogPotentiometer(0)
        self.motor = wpilib.VictorSP(6)
        self.setAbsoluteTolerance(.01)

    def initDefaultCommand(self):
        pass

    def manualSet(self, output):
        position = self.mast_pot.get()
        if position < self.kBackLimit and output < 0:
            self.motor.set(0)
        elif position > self.kForwardLimit and output > 0:
            self.motor.set(0)
        else:
            self.motor.set(output)

    def log(self):
        wpilib.SmartDashboard.putNumber("Angle Pot", self.mast_pot.get()) #publishes to the Dash

    def returnPIDInput(self):
        return self.mast_pot.get()

    def usePIDOutput(self, output):
        if output > 1:
            output = 1
        elif output < -1:
            output = -1
        self.motor.set(output*.38)

    def isBack(self):
        self.mast_pot.get() > self.kBack

    def isForward(self):
        not self.isBack()
