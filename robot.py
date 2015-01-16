#!/usr/bin/env python3
__author__ = 'nikolojedison'
#This code was written to test some things and may end up being used
#on the robot, but I dunno. So far it seems to work fine. Change what
#needs to be changed. Will evolve as time goes on.
#-Nik Mal

from networktables import NetworkTable
import wpilib
import logging
from .autonomous_utilities import Auto
from drive_control import *

logging.basicConfig(level=logging.DEBUG)

class Lopez_Jr(wpilib.SampleRobot):
    def robotInit(self):
        """initialises robot as a mecanum drive bot w/ 2 joysticks and a camera"""
        #want to change this to Xbox 360 controller eventually... probably sooner rather
        #than later.
        #
        #This is for a USB camera. Uncomment it if we aren't using the Axis.
        self.camera = wpilib.USBCamera()
        self.camera.setExposureManual(50)
        self.camera.setBrightness(80)
        self.camera.updateSettings()
        self.camera.setFPS(10)
        self.camera.setSize(320, 240)
        self.camera.setWhiteBalanceAuto()
        self.camera.setQuality(30)
        
        server = wpilib.CameraServer.getInstance()
        server.startAutomaticCapture(camera)
        
        self.drive = wpilib.RobotDrive(3, 1, 2, 0)
        self.drive.setExpiration(0.1)
        
        self.stick_left = wpilib.Joystick(0)
        self.stick_right = wpilib.Joystick(1)
        
        self.drive.setInvertedMotor(self.drive.MotorType.kFrontRight, True)
        self.drive.setInvertedMotor(self.drive.MotorType.kRearRight, True)
        
        self.gyro = wpilib.Gyro(0)
        
        self.aux_left = wpilib.Jaguar(6)
        self.aux_right = wpilib.Jaguar(4)
        self.window_motor = wpilib.Jaguar(5)
        
        self.smart_dashboard = NetworkTable.getTable("SmartDashboard")

    def autonomous(self):
        """Woo, auton code. Needs to be tested."""
        auto = Auto(self)
        auto_program_one = self.smart_dashboard.getBoolean("Auto Button 1", defaultValue=False) #If the dashboard hasn't set the value, it's False by default.
        auto_program_two = self.smart_dashboard.getBoolean("Auto Button 2", defaultValue=False)

        if auto_program_two:
            #Do the thing if the button's pushed
            auto.tote_grabba()
            auto.tote_lift(1)
            auto.can_slappa()
            auto.forward(1)
            auto.tote_releasa()
            auto.tote_lower(1)
            auto.tote_grabba()
            auto.tote_lift(1)
            auto.can_slappa()
            auto.forward(1)
            auto.tote_releasa()
            auto.tote_lower(1)
            auto.tote_grabba()
            auto.tote_lift(1)
            
        elif auto_program_two: #this is the simple auton that was talked about.
            auto.forward(5)
        else:
            #Neither are pushed


    def operatorControl(self):
        """Runs the drive with mecanum steering. Other motors added as needed."""

        self.drive.setSafetyEnabled(True)

        while self.isOperatorControl() and self.isEnabled():
            precision = self.stick_right.getRawButton(1)
            x = drive_control(self.stick_right.getX(), precision)
            y = drive_control(self.stick_right.getY(), precision)
            z = drive_control(self.stick_right.getZ(), precision)

            aux = dead_zone(self.stick_left.getY())
            window_motor = dead_zone(self.stick_left.getX())
            self.smart_dashboard.putNumber("Gyro",self.gyro.getAngle())

            gyro_angle = 0

            self.drive.mecanumDrive_Cartesian(x, y, z, 0)   # mecanum drive

            self.aux_left.set(aux) # auxiliary left miniCIM
            self.aux_right.set(aux)# auxiliary right miniCIM
            self.window_motor.set(window_motor) # random window motor that electrical hooked up

            wpilib.Timer.delay(.005)    # don't burn up the cpu

    def test(self):
        """no tests yet, woo"""
        pass

if __name__ == "__main__":
    wpilib.run(Lopez_Jr)
