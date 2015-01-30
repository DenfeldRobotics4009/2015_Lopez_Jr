import math

import wpilib
from wpilib.command import Subsystem

from commands.MecanumDriveWithJoystick import MecanumDriveWithJoystick

class Drivetrain(Subsystem):
    '''Class drivetrain uses a few Talons to run a 'bot.
    '''
    
    def __init__(self, robot):
        super().__init__()
        self.robot = robot
        
        self.drive = wpilib.RobotDrive(3, 1, 2, 0)
        self.drive.setExpiration(0.1)
        
        self.drive.setInvertedMotor(self.drive.MotorType.kFrontRight, True)
        self.drive.setInvertedMotor(self.drive.MotorType.kRearRight, True)
        
        
    def initDefaultCommand(self):
        '''When no other command is running let the operator drive around
           using the joystick'''
        self.setDefaultCommand(MecanumDriveWithJoystick(self.robot))
