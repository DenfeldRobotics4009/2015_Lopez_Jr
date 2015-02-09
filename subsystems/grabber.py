__author__ = 'nikolojedison'
import wpilib
from wpilib.command import PIDSubsystem

class Grabber(PIDSubsystem):
    kOpen = .122
    kClose = .850
    def __init__(self, robot):
        super().__init__(20, 0, 0)
        self.robot = robot

        self.grabba_pot = wpilib.AnalogPotentiometer(2)
        self.motor = wpilib.Jaguar(4)
        self.current = wpilib.AnalogInput(3)
        self.setAbsoluteTolerance(.01)

    def initDefaultCommand(self):
        pass

    def log(self):
        wpilib.SmartDashboard.putNumber("Clamp Pot", self.grabba_pot.get()) #publishes to the Dash
        wpilib.SmartDashboard.putNumber("Current Regulator", self.current.getVoltage())

    def manualSet(self, output):
        position = self.grabba_pot.get()
        if position > self.kClose and output > 0:
            self.motor.set(0)
        elif position < self.kOpen and output < 0:
            self.motor.set(0)
        else:
            self.motor.set(output)

    def returnPIDInput(self):
        return self.grabba_pot.get()

    def usePIDOutput(self, output):
        self.motor.set(output)
