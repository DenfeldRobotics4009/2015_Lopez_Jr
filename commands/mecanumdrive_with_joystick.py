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
        
    def initialize(self):
        '''Called just before this Command runs the first time'''
    
    def execute(self):
        '''Called repeatedly when this Command is scheduled to run'''
        self.robot.drivetrain.driveJoystick(self.robot.oi.getJoystick())
        
    def isFinished(self):
        '''Make this return true when this Command no longer needs to run execute()'''
        return False # Runs until interrupted
    
    def end(self):
        '''Called once after isFinished returns true'''
        self.robot.drivetrain.driveManual(0, 0)
        
    def interrupted(self):
        '''Called when another command which requires one or more of the same
           subsystems is scheduled to run'''
        self.end()