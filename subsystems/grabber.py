__author__ = 'nikolojedison'
from wpilib.command import PIDSubsystem

class Grabber(PIDSubsystem):

    def __init__(self, robot)
        super().__init__()
        self.robot = robot
        
        self.grabba_pot = wpilib.AnalogPotentiometer(1)
        
        self.grabba_pid = wpilib.PIDController(4, 0.07, 0, self.grabba_pot.pidGet, self.window_motor.pidWrite)
        self.grabba_pid.disable()


    def initDefaultCommand(self):
        pass
    
    def log(self):
        wpilib.SmartDashboard.putNumber("Grabba Pot", self.grabba_pot.get())
