__author__ = 'nikolojedison'

from wpilib.command import Command

class MecanumDriveWithJoystick(Command):
    '''
        Have the robot drive mecanum style using the joystick until interrupted.
    '''
    
    def __init__(self, robot):
        super().__init__()
        
        self.robot = robot
        self.requires(self.robot.drivetrain)
    
    def execute(self):
        self.robot.drivetrain.driveJoystick(self.robot.oi.getJoystick())
        
    def isFinished(self):
        return False # Runs until interrupted
    
    def end(self):
        self.robot.drivetrain.driveManual(0,0,0)
        pass
        
    def interrupted(self):
        self.end()