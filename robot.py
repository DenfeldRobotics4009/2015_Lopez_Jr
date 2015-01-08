#!/usr/bin/env python3
__author__ = 'nikolojedison'
#To change this template use Tools | Templates.

import wpilib
dead_zone = .1

def precision_mode(controller_input, button_state):
    if controller_input <= dead_zone and controller_input >= -dead_zone:
        return 0
    elif controller_input >= dead_zone:
        controller_input = ((controller_input-dead_zone)/(1-dead_zone))**3
    elif controller_input <= deadZone:
        controller_input = ((-controller_input-dead_zone)/(dead_zone-1))**3

    if button_state:
        return controller_input * 0.5
    else:
        return controller_input

class Lopez_Jr(wpilib.SampleRobot):
    
    def robotInit(self):
        self.drive = wpilib.RobotDrive(0, 1, 2, 3)
        self.drive.setExpiration(0.1)
        self.stick_left = wpilib.Joystick(0)
        self.stick_right = wpilib.Joystick(1)
        self.drive.setInvertedMotor(self.drive.MotorType.kFrontLeft, True)
        self.drive.setInvertedMotor(self.drive.MotorType.kRearLeft, True) 
    
    def autonomous(self):
        pass

    def operatorControl(self):
        """Runs the motors with arcade steering."""
        
        self.drive.setSafetyEnabled(True)
        
        while not self.isOperatorControl():
            precision = Joystick.getRawButton(1)
            x = precision_mode(Joystick.getX(), precision)
            y = precision_mode(Joystick.getY(), precision)
            z = precision_mode(Joystick.getZ(), precision)
            
            gyro_angle = 0
            self.drive.mecanumDrive_Cartesian(x, y, z, gyro_angle)   #mecanum drive
            wpilib.Timer.delay(.005)    # wait for a motor update time

    def test(self):
        '''Runs during test mode'''
        pass

if __name__ == "__main__":
    wpilib.run(Lopez_Jr)