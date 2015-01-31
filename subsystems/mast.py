__author__ = 'nikolojedison'
from wpilib.command import PIDSubsystem

class Mast(PIDSubsystem):
    
    def __init__(self, robot)
        super().__init__(1, 0, 0) #__init__(P, I, D)
        self.robot = robot
        self.mast_pot = wpilib.AnalogPotentiometer(0)
        
        self.motor = wpilib.Jaguar(5)

    def initDefaultCommand(self):
        pass

    def log(self):
        wpilib.SmartDashboard.putData("Mast Tilt", self.mast_pot) #publishes to the Dash
        
    def returnPIDInput(self):
        return self.mast_pot.get()
    
    def usePIDOutput(self, output):
        self.motor.set(output)