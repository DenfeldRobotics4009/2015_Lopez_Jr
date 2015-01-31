__author__ = 'nikolojedison'
from wpilib.command import PIDSubsystem

class Lift(PIDSubsystem):

    def __init__(self, robot)
        super().__init__()
        self.robot = robot
        
        self.lift_pot = wpilib.AnalogPotentiometer(2)
        
        self.lift_pid = wpilib.PIDController(4, 0.07, 0, self.lift_pot.pidGet, aux_combined)
        self.lift_pid.disable()

    def initDefaultCommand(self):
        pass
