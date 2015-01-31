import math

import wpilib
from wpilib.command import Subsystem
from commands.mecanum_drive_with_joystick import MecanumDriveWithJoystick
from drive_control import drive_control
from imu_simple import IMUSimple
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
        
        self.gyro = IMUSimple()


    def initDefaultCommand(self):
        '''When no other command is running let the operator drive around
           using the joystick'''
        self.setDefaultCommand(MecanumDriveWithJoystick(self.robot))
       
    def log(self):
        wpilib.SmartDashboard.putNumber("Gyro", self.gyro.getYaw())

    def driveJoystick(self, joystick):
        precision = joystick.getRawButton(0)
        x = drive_control(self.stick_right.getX(), precision)
        y = drive_control(self.stick_right.getY(), precision)
        z = drive_control(self.stick_right.getZ(), precision)
        self.driveManual(x,y,z)

    def driveManual(self, x, y , rotation):
        self.drive.mecanumDrive_Cartesian(x, y, rotation, 0)
